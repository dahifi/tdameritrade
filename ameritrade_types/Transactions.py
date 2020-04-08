from .Utils import *


class Instrument:
    def __init__(self, symbol, underlying_symbol, option_expiration_date, option_strike_price, put_call, cusip, description, asset_type, bond_maturity_date, bond_interest_rate):
        self.symbol = symbol
        self.underlying_symbol = underlying_symbol
        self.option_expiration_date = option_expiration_date
        self.option_strike_price = option_strike_price
        self.put_call = put_call
        self.cusip = cusip
        self.description = description
        self.asset_type = asset_type
        self.bond_maturity_date = bond_maturity_date
        self.bond_interest_rate = bond_interest_rate

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        symbol = from_str(obj.get("symbol"))
        underlying_symbol = from_str(obj.get("underlyingSymbol"))
        option_expiration_date = from_str(obj.get("optionExpirationDate"))
        option_strike_price = from_int(obj.get("optionStrikePrice"))
        put_call = from_str(obj.get("putCall"))
        cusip = from_str(obj.get("cusip"))
        description = from_str(obj.get("description"))
        asset_type = from_str(obj.get("assetType"))
        bond_maturity_date = from_str(obj.get("bondMaturityDate"))
        bond_interest_rate = from_int(obj.get("bondInterestRate"))
        return Instrument(symbol, underlying_symbol, option_expiration_date, option_strike_price, put_call, cusip, description, asset_type, bond_maturity_date, bond_interest_rate)

    def to_dict(self):
        result = {}
        result["symbol"] = from_str(self.symbol)
        result["underlyingSymbol"] = from_str(self.underlying_symbol)
        result["optionExpirationDate"] = from_str(self.option_expiration_date)
        result["optionStrikePrice"] = from_int(self.option_strike_price)
        result["putCall"] = from_str(self.put_call)
        result["cusip"] = from_str(self.cusip)
        result["description"] = from_str(self.description)
        result["assetType"] = from_str(self.asset_type)
        result["bondMaturityDate"] = from_str(self.bond_maturity_date)
        result["bondInterestRate"] = from_int(self.bond_interest_rate)
        return result


class TransactionItem:
    def __init__(self, account_id, amount, price, cost, parent_order_key, parent_child_indicator, instruction, position_effect, instrument):
        self.account_id = account_id
        self.amount = amount
        self.price = price
        self.cost = cost
        self.parent_order_key = parent_order_key
        self.parent_child_indicator = parent_child_indicator
        self.instruction = instruction
        self.position_effect = position_effect
        self.instrument = instrument

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        account_id = from_int(obj.get("accountId"))
        amount = from_int(obj.get("amount"))
        price = from_int(obj.get("price"))
        cost = from_int(obj.get("cost"))
        parent_order_key = from_int(obj.get("parentOrderKey"))
        parent_child_indicator = from_str(obj.get("parentChildIndicator"))
        instruction = from_str(obj.get("instruction"))
        position_effect = from_str(obj.get("positionEffect"))
        instrument = Instrument.from_dict(obj.get("instrument"))
        return TransactionItem(account_id, amount, price, cost, parent_order_key, parent_child_indicator, instruction, position_effect, instrument)

    def to_dict(self):
        result = {}
        result["accountId"] = from_int(self.account_id)
        result["amount"] = from_int(self.amount)
        result["price"] = from_int(self.price)
        result["cost"] = from_int(self.cost)
        result["parentOrderKey"] = from_int(self.parent_order_key)
        result["parentChildIndicator"] = from_str(self.parent_child_indicator)
        result["instruction"] = from_str(self.instruction)
        result["positionEffect"] = from_str(self.position_effect)
        result["instrument"] = to_class(Instrument, self.instrument)
        return result


class Transactions:
    def __init__(self, type, clearing_reference_number, sub_account, settlement_date, order_id, sma, requirement_reallocation_amount, day_trade_buying_power_effect, net_amount,
                 transaction_date, order_date, transaction_sub_type, transaction_id, cash_balance_effect_flag, description, ach_status, accrued_interest, fees, transaction_item):
        self.type = type
        self.clearing_reference_number = clearing_reference_number
        self.sub_account = sub_account
        self.settlement_date = settlement_date
        self.order_id = order_id
        self.sma = sma
        self.requirement_reallocation_amount = requirement_reallocation_amount
        self.day_trade_buying_power_effect = day_trade_buying_power_effect
        self.net_amount = net_amount
        self.transaction_date = transaction_date
        self.order_date = order_date
        self.transaction_sub_type = transaction_sub_type
        self.transaction_id = transaction_id
        self.cash_balance_effect_flag = cash_balance_effect_flag
        self.description = description
        self.ach_status = ach_status
        self.accrued_interest = accrued_interest
        self.fees = fees
        self.transaction_item = transaction_item

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        clearing_reference_number = from_str(obj.get("clearingReferenceNumber"))
        sub_account = from_str(obj.get("subAccount"))
        settlement_date = from_str(obj.get("settlementDate"))
        order_id = from_str(obj.get("orderId"))
        sma = from_int(obj.get("sma"))
        requirement_reallocation_amount = from_int(obj.get("requirementReallocationAmount"))
        day_trade_buying_power_effect = from_int(obj.get("dayTradeBuyingPowerEffect"))
        net_amount = from_int(obj.get("netAmount"))
        transaction_date = from_str(obj.get("transactionDate"))
        order_date = from_str(obj.get("orderDate"))
        transaction_sub_type = from_str(obj.get("transactionSubType"))
        transaction_id = from_int(obj.get("transactionId"))
        cash_balance_effect_flag = from_bool(obj.get("cashBalanceEffectFlag"))
        description = from_str(obj.get("description"))
        ach_status = from_str(obj.get("achStatus"))
        accrued_interest = from_int(obj.get("accruedInterest"))
        fees = from_str(obj.get("fees"))
        transaction_item = TransactionItem.from_dict(obj.get("transactionItem"))
        return Transactions(type, clearing_reference_number, sub_account, settlement_date, order_id, sma, requirement_reallocation_amount, day_trade_buying_power_effect, net_amount,
                            transaction_date, order_date, transaction_sub_type, transaction_id, cash_balance_effect_flag, description, ach_status, accrued_interest, fees, transaction_item)

    def to_dict(self):
        result = {}
        result["type"] = from_str(self.type)
        result["clearingReferenceNumber"] = from_str(self.clearing_reference_number)
        result["subAccount"] = from_str(self.sub_account)
        result["settlementDate"] = from_str(self.settlement_date)
        result["orderId"] = from_str(self.order_id)
        result["sma"] = from_int(self.sma)
        result["requirementReallocationAmount"] = from_int(self.requirement_reallocation_amount)
        result["dayTradeBuyingPowerEffect"] = from_int(self.day_trade_buying_power_effect)
        result["netAmount"] = from_int(self.net_amount)
        result["transactionDate"] = from_str(self.transaction_date)
        result["orderDate"] = from_str(self.order_date)
        result["transactionSubType"] = from_str(self.transaction_sub_type)
        result["transactionId"] = from_int(self.transaction_id)
        result["cashBalanceEffectFlag"] = from_bool(self.cash_balance_effect_flag)
        result["description"] = from_str(self.description)
        result["achStatus"] = from_str(self.ach_status)
        result["accruedInterest"] = from_int(self.accrued_interest)
        result["fees"] = from_str(self.fees)
        result["transactionItem"] = to_class(TransactionItem, self.transaction_item)
        return result


def transactions_from_dict(s):
    return Transactions.from_dict(s)


def transactions_to_dict(x):
    return to_class(Transactions, x)
