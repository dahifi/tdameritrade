import pandas as pd
from .session import TDASession
from .urls import ACCOUNTS, INSTRUMENTS, QUOTES, SEARCH, HISTORY, OPTIONCHAIN, MOVERS
from .exceptions import handle_error_response


def response_is_valid(resp):
    valid_codes = [200, 201]
    return resp.status_code in valid_codes


class TDClient(object):
    def __init__(self, client_id=None, refresh_token=None, account_ids=[]):
        self._clientId = client_id
        self._refreshToken = refresh_token
        self.accountIds = account_ids
        self.session = TDASession(self._refreshToken, self._clientId)

    def _request(self, url, method="GET", params=None, *args, **kwargs):
        resp = self.session.request(method, url, params=params, *args, **kwargs)
        if not response_is_valid(resp):
            handle_error_response(resp)

        return resp

    # TODO: output results to self.accountIds
    def accounts(self, positions=False, orders=False):
        ret = {}

        if positions or orders:
            fields = '?fields='
            if positions:
                fields += 'positions'
                if orders:
                    fields += ',orders'
            elif orders:
                fields += 'orders'
        else:
            fields = ''

        if self.accountIds:
            for acc in self.accountIds:
                resp = self._request(ACCOUNTS + str(acc) + fields)
                ret[acc] = resp.json()

        else:
            resp = self._request(ACCOUNTS + fields)
            for account in resp.json():
                ret[account['securitiesAccount']['accountId']] = account

        return ret

    def accountsDF(self):
        return pd.json_normalize(self.accounts())

    def transactions(self, acc=None, type=None, symbol=None, start_date=None, end_date=None):
        if acc is None:
            acc = self.accounts
        transactions = ACCOUNTS + str(acc) + "/transactions"
        resp = self._request(transactions,
                             params={
                                 'type': type,
                                 'symbol': symbol,
                                 'startDate': start_date,
                                 'endDate': end_date
                             }).json()

        return resp

    def transactionsDF(self, acc, **kwargs):
        return pd.json_normalize(self.transactions(acc, kwargs))

    def search(self, symbol, projection='symbol-search'):
        resp = self._request(SEARCH,
                             params={'symbol': symbol,
                                     'projection': projection}).json()
        return resp

    def searchDF(self, symbol, projection='symbol-search'):
        ret = []
        dat = self.search(symbol, projection)
        for symbol in dat:
            ret.append(dat[symbol])

        return pd.DataFrame(ret)

    def fundamental(self, symbol):
        return self.search(symbol, 'fundamental')

    def fundamentalDF(self, symbol):
        return self.searchDF(symbol, 'fundamental')

    def instrument(self, cusip):
        resp = self._request(INSTRUMENTS + str(cusip)).json()
        return resp

    def instrumentDF(self, cusip):
        return pd.DataFrame(self.instrument(cusip))

    def quote(self, symbol):
        resp = self._request(QUOTES,
                             params={'symbol': symbol.upper()}).json()
        return resp

    def quoteDF(self, symbol):
        x = self.quote(symbol)

        return pd.DataFrame(x).T.reset_index(drop=True)

    def history(self, symbol, **kwargs):
        resp = self._request(HISTORY % symbol,
                             params=kwargs).json()
        return resp

    def historyDF(self, symbol, **kwargs):
        x = self.history(symbol, **kwargs)
        df = pd.DataFrame(x['candles'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')

        return df

    def options(self, symbol, **kwargs):
        resp = self._request(OPTIONCHAIN,
                             params={'symbol': symbol.upper(), **kwargs}).json()
        return resp

    def optionsDF(self, symbol):
        ret = []
        dat = self.options(symbol)
        for date in dat['callExpDateMap']:
            for strike in dat['callExpDateMap'][date]:
                ret.extend(dat['callExpDateMap'][date][strike])
        for date in dat['putExpDateMap']:
            for strike in dat['putExpDateMap'][date]:
                ret.extend(dat['putExpDateMap'][date][strike])

        df = pd.DataFrame(ret)
        for col in ('tradeTimeInLong', 'quoteTimeInLong',
                    'expirationDate', 'lastTradingDay'):
            df[col] = pd.to_datetime(df[col], unit='ms')

        return df

    def movers(self, index, direction='up', change_type='percent'):
        resp = self._request(MOVERS % index,
                             params={'direction': direction,
                                     'change_type': change_type}).json()
        return resp

    def create_saved_order(self, account_id, json_order):
        saved_orders = ACCOUNTS + account_id + "/savedorders"
        resp = self._request(saved_orders,
                             method="POST",
                             json=json_order)
        return resp

    def place_order(self, account_id, json_order):
        orders = ACCOUNTS + account_id + "/orders"
        resp = self._request(orders,
                             method="POST",
                             json=json_order)
        return resp
