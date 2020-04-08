# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = quotes_from_dict(json.loads(json_string))


def from_float(x):
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_none(x):
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except BaseException:
            pass
    assert False


def from_str(x):
    assert isinstance(x, str)
    return x


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x):
    assert isinstance(x, bool)
    return x


def to_float(x):
    assert isinstance(x, float)
    return x


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Equity:
    def __init__(self, the_52_wk_high, the_52_wk_low, ask_id, ask_price, ask_size, bid_id, bid_price, bid_size, close_price, description, digits, div_amount, div_date, div_yield, exchange, exchange_name, high_price, last_id, last_price, last_size, low_price, marginable,
                 mark, net_change, open_price, pe_ratio, quote_time_in_long, regular_market_last_price, regular_market_last_size, regular_market_net_change, regular_market_trade_time_in_long, security_status, shortable, symbol, total_volume, trade_time_in_long, volatility):
        self.the_52_wk_high = the_52_wk_high
        self.the_52_wk_low = the_52_wk_low
        self.ask_id = ask_id
        self.ask_price = ask_price
        self.ask_size = ask_size
        self.bid_id = bid_id
        self.bid_price = bid_price
        self.bid_size = bid_size
        self.close_price = close_price
        self.description = description
        self.digits = digits
        self.div_amount = div_amount
        self.div_date = div_date
        self.div_yield = div_yield
        self.exchange = exchange
        self.exchange_name = exchange_name
        self.high_price = high_price
        self.last_id = last_id
        self.last_price = last_price
        self.last_size = last_size
        self.low_price = low_price
        self.marginable = marginable
        self.mark = mark
        self.net_change = net_change
        self.open_price = open_price
        self.pe_ratio = pe_ratio
        self.quote_time_in_long = quote_time_in_long
        self.regular_market_last_price = regular_market_last_price
        self.regular_market_last_size = regular_market_last_size
        self.regular_market_net_change = regular_market_net_change
        self.regular_market_trade_time_in_long = regular_market_trade_time_in_long
        self.security_status = security_status
        self.shortable = shortable
        self.symbol = symbol
        self.total_volume = total_volume
        self.trade_time_in_long = trade_time_in_long
        self.volatility = volatility

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        the_52_wk_high = from_union([from_float, from_none], obj.get("52WkHigh"))
        the_52_wk_low = from_union([from_float, from_none], obj.get("52WkLow"))
        ask_id = from_union([from_str, from_none], obj.get("askId"))
        ask_price = from_union([from_float, from_none], obj.get("askPrice"))
        ask_size = from_union([from_int, from_none], obj.get("askSize"))
        bid_id = from_union([from_str, from_none], obj.get("bidId"))
        bid_price = from_union([from_float, from_none], obj.get("bidPrice"))
        bid_size = from_union([from_int, from_none], obj.get("bidSize"))
        close_price = from_union([from_float, from_none], obj.get("closePrice"))
        description = from_union([from_str, from_none], obj.get("description"))
        digits = from_union([from_int, from_none], obj.get("digits"))
        div_amount = from_union([from_float, from_none], obj.get("divAmount"))
        div_date = from_union([from_str, from_none], obj.get("divDate"))
        div_yield = from_union([from_float, from_none], obj.get("divYield"))
        exchange = from_union([from_str, from_none], obj.get("exchange"))
        exchange_name = from_union([from_str, from_none], obj.get("exchangeName"))
        high_price = from_union([from_float, from_none], obj.get("highPrice"))
        last_id = from_union([from_str, from_none], obj.get("lastId"))
        last_price = from_union([from_float, from_none], obj.get("lastPrice"))
        last_size = from_union([from_int, from_none], obj.get("lastSize"))
        low_price = from_union([from_float, from_none], obj.get("lowPrice"))
        marginable = from_union([from_bool, from_none], obj.get("marginable"))
        mark = from_union([from_float, from_none], obj.get("mark"))
        net_change = from_union([from_float, from_none], obj.get("netChange"))
        open_price = from_union([from_float, from_none], obj.get("openPrice"))
        pe_ratio = from_union([from_float, from_none], obj.get("peRatio"))
        quote_time_in_long = from_union([from_int, from_none], obj.get("quoteTimeInLong"))
        regular_market_last_price = from_union([from_float, from_none], obj.get("regularMarketLastPrice"))
        regular_market_last_size = from_union([from_int, from_none], obj.get("regularMarketLastSize"))
        regular_market_net_change = from_union([from_float, from_none], obj.get("regularMarketNetChange"))
        regular_market_trade_time_in_long = from_union([from_int, from_none], obj.get("regularMarketTradeTimeInLong"))
        security_status = from_union([from_str, from_none], obj.get("securityStatus"))
        shortable = from_union([from_bool, from_none], obj.get("shortable"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        total_volume = from_union([from_int, from_none], obj.get("totalVolume"))
        trade_time_in_long = from_union([from_int, from_none], obj.get("tradeTimeInLong"))
        volatility = from_union([from_float, from_none], obj.get("volatility"))
        return Equity(the_52_wk_high, the_52_wk_low, ask_id, ask_price, ask_size, bid_id, bid_price, bid_size, close_price, description, digits, div_amount, div_date, div_yield, exchange, exchange_name, high_price, last_id, last_price, last_size, low_price, marginable,
                      mark, net_change, open_price, pe_ratio, quote_time_in_long, regular_market_last_price, regular_market_last_size, regular_market_net_change, regular_market_trade_time_in_long, security_status, shortable, symbol, total_volume, trade_time_in_long, volatility)

    def to_dict(self):
        result = {}
        result["52WkHigh"] = from_union([to_float, from_none], self.the_52_wk_high)
        result["52WkLow"] = from_union([to_float, from_none], self.the_52_wk_low)
        result["askId"] = from_union([from_str, from_none], self.ask_id)
        result["askPrice"] = from_union([to_float, from_none], self.ask_price)
        result["askSize"] = from_union([from_int, from_none], self.ask_size)
        result["bidId"] = from_union([from_str, from_none], self.bid_id)
        result["bidPrice"] = from_union([to_float, from_none], self.bid_price)
        result["bidSize"] = from_union([from_int, from_none], self.bid_size)
        result["closePrice"] = from_union([to_float, from_none], self.close_price)
        result["description"] = from_union([from_str, from_none], self.description)
        result["digits"] = from_union([from_int, from_none], self.digits)
        result["divAmount"] = from_union([to_float, from_none], self.div_amount)
        result["divDate"] = from_union([from_str, from_none], self.div_date)
        result["divYield"] = from_union([to_float, from_none], self.div_yield)
        result["exchange"] = from_union([from_str, from_none], self.exchange)
        result["exchangeName"] = from_union([from_str, from_none], self.exchange_name)
        result["highPrice"] = from_union([to_float, from_none], self.high_price)
        result["lastId"] = from_union([from_str, from_none], self.last_id)
        result["lastPrice"] = from_union([to_float, from_none], self.last_price)
        result["lastSize"] = from_union([from_int, from_none], self.last_size)
        result["lowPrice"] = from_union([to_float, from_none], self.low_price)
        result["marginable"] = from_union([from_bool, from_none], self.marginable)
        result["mark"] = from_union([to_float, from_none], self.mark)
        result["netChange"] = from_union([to_float, from_none], self.net_change)
        result["openPrice"] = from_union([to_float, from_none], self.open_price)
        result["peRatio"] = from_union([to_float, from_none], self.pe_ratio)
        result["quoteTimeInLong"] = from_union([from_int, from_none], self.quote_time_in_long)
        result["regularMarketLastPrice"] = from_union([to_float, from_none], self.regular_market_last_price)
        result["regularMarketLastSize"] = from_union([from_int, from_none], self.regular_market_last_size)
        result["regularMarketNetChange"] = from_union([to_float, from_none], self.regular_market_net_change)
        result["regularMarketTradeTimeInLong"] = from_union([from_int, from_none], self.regular_market_trade_time_in_long)
        result["securityStatus"] = from_union([from_str, from_none], self.security_status)
        result["shortable"] = from_union([from_bool, from_none], self.shortable)
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["totalVolume"] = from_union([from_int, from_none], self.total_volume)
        result["tradeTimeInLong"] = from_union([from_int, from_none], self.trade_time_in_long)
        result["volatility"] = from_union([to_float, from_none], self.volatility)
        return result


class Quotes:
    def __init__(self, equity):
        self.equity = equity

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        equity = from_union([Equity.from_dict, from_none], obj.get("Equity"))
        return Quotes(equity)

    def to_dict(self):
        result = {}
        result["Equity"] = from_union([lambda x: to_class(Equity, x), from_none], self.equity)
        return result


def quotes_from_dict(s):
    return Quotes.from_dict(s)


def quotes_to_dict(x):
    return to_class(Quotes, x)
