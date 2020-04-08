# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = accounts_from_dict(json.loads(json_string))

from enum import Enum
from datetime import datetime
import dateutil.parser


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


def to_float(x):
    assert isinstance(x, float)
    return x


def from_str(x):
    assert isinstance(x, str)
    return x


def from_bool(x):
    assert isinstance(x, bool)
    return x


def to_enum(c, x):
    assert isinstance(x, c)
    return x.value


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x):
    return dateutil.parser.parse(x)


class CurrentBalances:
    def __init__(self, accrued_interest, bond_value, cash_available_for_trading, cash_available_for_withdrawal, cash_balance, cash_call, cash_debit_call_value, cash_receipts, liquidation_value, long_market_value,
                 long_non_marginable_market_value, long_option_market_value, money_market_fund, mutual_fund_value, pending_deposits, savings, short_market_value, short_option_market_value, total_cash, unsettled_cash):
        self.accrued_interest = accrued_interest
        self.bond_value = bond_value
        self.cash_available_for_trading = cash_available_for_trading
        self.cash_available_for_withdrawal = cash_available_for_withdrawal
        self.cash_balance = cash_balance
        self.cash_call = cash_call
        self.cash_debit_call_value = cash_debit_call_value
        self.cash_receipts = cash_receipts
        self.liquidation_value = liquidation_value
        self.long_market_value = long_market_value
        self.long_non_marginable_market_value = long_non_marginable_market_value
        self.long_option_market_value = long_option_market_value
        self.money_market_fund = money_market_fund
        self.mutual_fund_value = mutual_fund_value
        self.pending_deposits = pending_deposits
        self.savings = savings
        self.short_market_value = short_market_value
        self.short_option_market_value = short_option_market_value
        self.total_cash = total_cash
        self.unsettled_cash = unsettled_cash

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        accrued_interest = from_union([from_float, from_none], obj.get("accruedInterest"))
        bond_value = from_union([from_float, from_none], obj.get("bondValue"))
        cash_available_for_trading = from_union([from_float, from_none], obj.get("cashAvailableForTrading"))
        cash_available_for_withdrawal = from_union([from_float, from_none], obj.get("cashAvailableForWithdrawal"))
        cash_balance = from_union([from_float, from_none], obj.get("cashBalance"))
        cash_call = from_union([from_float, from_none], obj.get("cashCall"))
        cash_debit_call_value = from_union([from_float, from_none], obj.get("cashDebitCallValue"))
        cash_receipts = from_union([from_float, from_none], obj.get("cashReceipts"))
        liquidation_value = from_union([from_float, from_none], obj.get("liquidationValue"))
        long_market_value = from_union([from_float, from_none], obj.get("longMarketValue"))
        long_non_marginable_market_value = from_union([from_float, from_none], obj.get("longNonMarginableMarketValue"))
        long_option_market_value = from_union([from_float, from_none], obj.get("longOptionMarketValue"))
        money_market_fund = from_union([from_float, from_none], obj.get("moneyMarketFund"))
        mutual_fund_value = from_union([from_float, from_none], obj.get("mutualFundValue"))
        pending_deposits = from_union([from_float, from_none], obj.get("pendingDeposits"))
        savings = from_union([from_float, from_none], obj.get("savings"))
        short_market_value = from_union([from_float, from_none], obj.get("shortMarketValue"))
        short_option_market_value = from_union([from_float, from_none], obj.get("shortOptionMarketValue"))
        total_cash = from_union([from_float, from_none], obj.get("totalCash"))
        unsettled_cash = from_union([from_float, from_none], obj.get("unsettledCash"))
        return CurrentBalances(accrued_interest, bond_value, cash_available_for_trading, cash_available_for_withdrawal, cash_balance, cash_call, cash_debit_call_value, cash_receipts, liquidation_value, long_market_value,
                               long_non_marginable_market_value, long_option_market_value, money_market_fund, mutual_fund_value, pending_deposits, savings, short_market_value, short_option_market_value, total_cash, unsettled_cash)

    def to_dict(self):
        result = {}
        result["accruedInterest"] = from_union([to_float, from_none], self.accrued_interest)
        result["bondValue"] = from_union([to_float, from_none], self.bond_value)
        result["cashAvailableForTrading"] = from_union([to_float, from_none], self.cash_available_for_trading)
        result["cashAvailableForWithdrawal"] = from_union([to_float, from_none], self.cash_available_for_withdrawal)
        result["cashBalance"] = from_union([to_float, from_none], self.cash_balance)
        result["cashCall"] = from_union([to_float, from_none], self.cash_call)
        result["cashDebitCallValue"] = from_union([to_float, from_none], self.cash_debit_call_value)
        result["cashReceipts"] = from_union([to_float, from_none], self.cash_receipts)
        result["liquidationValue"] = from_union([to_float, from_none], self.liquidation_value)
        result["longMarketValue"] = from_union([to_float, from_none], self.long_market_value)
        result["longNonMarginableMarketValue"] = from_union([to_float, from_none], self.long_non_marginable_market_value)
        result["longOptionMarketValue"] = from_union([to_float, from_none], self.long_option_market_value)
        result["moneyMarketFund"] = from_union([to_float, from_none], self.money_market_fund)
        result["mutualFundValue"] = from_union([to_float, from_none], self.mutual_fund_value)
        result["pendingDeposits"] = from_union([to_float, from_none], self.pending_deposits)
        result["savings"] = from_union([to_float, from_none], self.savings)
        result["shortMarketValue"] = from_union([to_float, from_none], self.short_market_value)
        result["shortOptionMarketValue"] = from_union([to_float, from_none], self.short_option_market_value)
        result["totalCash"] = from_union([to_float, from_none], self.total_cash)
        result["unsettledCash"] = from_union([to_float, from_none], self.unsettled_cash)
        return result


class CancelTime:
    def __init__(self, date, short_format):
        self.date = date
        self.short_format = short_format

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        date = from_union([from_str, from_none], obj.get("date"))
        short_format = from_union([from_bool, from_none], obj.get("shortFormat"))
        return CancelTime(date, short_format)

    def to_dict(self):
        result = {}
        result["date"] = from_union([from_str, from_none], self.date)
        result["shortFormat"] = from_union([from_bool, from_none], self.short_format)
        return result


class ComplexOrderStrategyType(Enum):
    BACK_RATIO = "BACK_RATIO"
    BUTTERFLY = "BUTTERFLY"
    CALENDAR = "CALENDAR"
    COLLAR_SYNTHETIC = "COLLAR_SYNTHETIC"
    COLLAR_WITH_STOCK = "COLLAR_WITH_STOCK"
    CONDOR = "CONDOR"
    COVERED = "COVERED"
    CUSTOM = "CUSTOM"
    DIAGONAL = "DIAGONAL"
    DOUBLE_DIAGONAL = "DOUBLE_DIAGONAL"
    IRON_CONDOR = "IRON_CONDOR"
    NONE = "NONE"
    STRADDLE = "STRADDLE"
    STRANGLE = "STRANGLE"
    UNBALANCED_BUTTERFLY = "UNBALANCED_BUTTERFLY"
    UNBALANCED_CONDOR = "UNBALANCED_CONDOR"
    UNBALANCED_IRON_CONDOR = "UNBALANCED_IRON_CONDOR"
    UNBALANCED_VERTICAL_ROLL = "UNBALANCED_VERTICAL_ROLL"
    VERTICAL = "VERTICAL"
    VERTICAL_ROLL = "VERTICAL_ROLL"


class Duration(Enum):
    DAY = "DAY"
    FILL_OR_KILL = "FILL_OR_KILL"
    GOOD_TILL_CANCEL = "GOOD_TILL_CANCEL"


class ActivityType(Enum):
    EXECUTION = "EXECUTION"
    ORDER_ACTION = "ORDER_ACTION"


class OrderActivityCollection:
    def __init__(self, activity_type):
        self.activity_type = activity_type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        activity_type = from_union([ActivityType, from_none], obj.get("activityType"))
        return OrderActivityCollection(activity_type)

    def to_dict(self):
        result = {}
        result["activityType"] = from_union([lambda x: to_enum(ActivityType, x), from_none], self.activity_type)
        return result


class Instruction(Enum):
    BUY = "BUY"
    BUY_TO_CLOSE = "BUY_TO_CLOSE"
    BUY_TO_COVER = "BUY_TO_COVER"
    BUY_TO_OPEN = "BUY_TO_OPEN"
    EXCHANGE = "EXCHANGE"
    SELL = "SELL"
    SELL_SHORT = "SELL_SHORT"
    SELL_TO_CLOSE = "SELL_TO_CLOSE"
    SELL_TO_OPEN = "SELL_TO_OPEN"


class AssetTypeEnum(Enum):
    CASH_EQUIVALENT = "CASH_EQUIVALENT"
    CURRENCY = "CURRENCY"
    EQUITY = "EQUITY"
    FIXED_INCOME = "FIXED_INCOME"
    INDEX = "INDEX"
    MUTUAL_FUND = "MUTUAL_FUND"
    OPTION = "OPTION"


class Instrument:
    def __init__(self, asset_type, cusip, description, symbol):
        self.asset_type = asset_type
        self.cusip = cusip
        self.description = description
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        asset_type = from_union([AssetTypeEnum, from_none], obj.get("assetType"))
        cusip = from_union([from_str, from_none], obj.get("cusip"))
        description = from_union([from_str, from_none], obj.get("description"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        return Instrument(asset_type, cusip, description, symbol)

    def to_dict(self):
        result = {}
        result["assetType"] = from_union([lambda x: to_enum(AssetTypeEnum, x), from_none], self.asset_type)
        result["cusip"] = from_union([from_str, from_none], self.cusip)
        result["description"] = from_union([from_str, from_none], self.description)
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        return result


class PositionEffect(Enum):
    AUTOMATIC = "AUTOMATIC"
    CLOSING = "CLOSING"
    OPENING = "OPENING"


class QuantityType(Enum):
    ALL_SHARES = "ALL_SHARES"
    DOLLARS = "DOLLARS"
    SHARES = "SHARES"


class OrderLegCollection:
    def __init__(self, instruction, instrument, leg_id, order_leg_type, position_effect, quantity, quantity_type):
        self.instruction = instruction
        self.instrument = instrument
        self.leg_id = leg_id
        self.order_leg_type = order_leg_type
        self.position_effect = position_effect
        self.quantity = quantity
        self.quantity_type = quantity_type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        instruction = from_union([Instruction, from_none], obj.get("instruction"))
        instrument = from_union([Instrument.from_dict, from_none], obj.get("instrument"))
        leg_id = from_union([from_int, from_none], obj.get("legId"))
        order_leg_type = from_union([AssetTypeEnum, from_none], obj.get("orderLegType"))
        position_effect = from_union([PositionEffect, from_none], obj.get("positionEffect"))
        quantity = from_union([from_float, from_none], obj.get("quantity"))
        quantity_type = from_union([QuantityType, from_none], obj.get("quantityType"))
        return OrderLegCollection(instruction, instrument, leg_id, order_leg_type, position_effect, quantity, quantity_type)

    def to_dict(self):
        result = {}
        result["instruction"] = from_union([lambda x: to_enum(Instruction, x), from_none], self.instruction)
        result["instrument"] = from_union([lambda x: to_class(Instrument, x), from_none], self.instrument)
        result["legId"] = from_union([from_int, from_none], self.leg_id)
        result["orderLegType"] = from_union([lambda x: to_enum(AssetTypeEnum, x), from_none], self.order_leg_type)
        result["positionEffect"] = from_union([lambda x: to_enum(PositionEffect, x), from_none], self.position_effect)
        result["quantity"] = from_union([to_float, from_none], self.quantity)
        result["quantityType"] = from_union([lambda x: to_enum(QuantityType, x), from_none], self.quantity_type)
        return result


class OrderStrategyType(Enum):
    OCO = "OCO"
    SINGLE = "SINGLE"
    TRIGGER = "TRIGGER"


class OrderType(Enum):
    EXERCISE = "EXERCISE"
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"
    NET_CREDIT = "NET_CREDIT"
    NET_DEBIT = "NET_DEBIT"
    NET_ZERO = "NET_ZERO"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"
    TRAILING_STOP = "TRAILING_STOP"
    TRAILING_STOP_LIMIT = "TRAILING_STOP_LIMIT"


class PriceLinkBasis(Enum):
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    AVERAGE = "AVERAGE"
    BASE = "BASE"
    BID = "BID"
    LAST = "LAST"
    MANUAL = "MANUAL"
    MARK = "MARK"
    TRIGGER = "TRIGGER"


class PriceLinkType(Enum):
    PERCENT = "PERCENT"
    TICK = "TICK"
    VALUE = "VALUE"


class RequestedDestination(Enum):
    AMEX = "AMEX"
    AUTO = "AUTO"
    BATS = "BATS"
    BOX = "BOX"
    C2 = "C2"
    CBOE = "CBOE"
    ECN_ARCA = "ECN_ARCA"
    INET = "INET"
    ISE = "ISE"
    NASDAQ = "NASDAQ"
    NYSE = "NYSE"
    PHLX = "PHLX"


class Session(Enum):
    AM = "AM"
    NORMAL = "NORMAL"
    PM = "PM"
    SEAMLESS = "SEAMLESS"


class SpecialInstruction(Enum):
    ALL_OR_NONE = "ALL_OR_NONE"
    ALL_OR_NONE_DO_NOT_REDUCE = "ALL_OR_NONE_DO_NOT_REDUCE"
    DO_NOT_REDUCE = "DO_NOT_REDUCE"


class Status(Enum):
    ACCEPTED = "ACCEPTED"
    AWAITING_CONDITION = "AWAITING_CONDITION"
    AWAITING_MANUAL_REVIEW = "AWAITING_MANUAL_REVIEW"
    AWAITING_PARENT_ORDER = "AWAITING_PARENT_ORDER"
    AWAITING_UR_OUT = "AWAITING_UR_OUT"
    CANCELED = "CANCELED"
    EXPIRED = "EXPIRED"
    FILLED = "FILLED"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"
    PENDING_CANCEL = "PENDING_CANCEL"
    PENDING_REPLACE = "PENDING_REPLACE"
    QUEUED = "QUEUED"
    REJECTED = "REJECTED"
    REPLACED = "REPLACED"
    WORKING = "WORKING"


class StopType(Enum):
    ASK = "ASK"
    BID = "BID"
    LAST = "LAST"
    MARK = "MARK"
    STANDARD = "STANDARD"


class TaxLotMethod(Enum):
    AVERAGE_COST = "AVERAGE_COST"
    FIFO = "FIFO"
    HIGH_COST = "HIGH_COST"
    LIFO = "LIFO"
    LOW_COST = "LOW_COST"
    SPECIFIC_LOT = "SPECIFIC_LOT"


class OrderStrategy:
    def __init__(self, account_id, activation_price, cancelable, cancel_time, child_order_strategies, close_time, complex_order_strategy_type, destination_link_name, duration, editable, entered_time, filled_quantity, order_activity_collection, order_id, order_leg_collection, order_strategy_type, order_type,
                 price, price_link_basis, price_link_type, quantity, release_time, remaining_quantity, replacing_order_collection, requested_destination, session, special_instruction, status, status_description, stop_price, stop_price_link_basis, stop_price_link_type, stop_price_offset, stop_type, tag, tax_lot_method):
        self.account_id = account_id
        self.activation_price = activation_price
        self.cancelable = cancelable
        self.cancel_time = cancel_time
        self.child_order_strategies = child_order_strategies
        self.close_time = close_time
        self.complex_order_strategy_type = complex_order_strategy_type
        self.destination_link_name = destination_link_name
        self.duration = duration
        self.editable = editable
        self.entered_time = entered_time
        self.filled_quantity = filled_quantity
        self.order_activity_collection = order_activity_collection
        self.order_id = order_id
        self.order_leg_collection = order_leg_collection
        self.order_strategy_type = order_strategy_type
        self.order_type = order_type
        self.price = price
        self.price_link_basis = price_link_basis
        self.price_link_type = price_link_type
        self.quantity = quantity
        self.release_time = release_time
        self.remaining_quantity = remaining_quantity
        self.replacing_order_collection = replacing_order_collection
        self.requested_destination = requested_destination
        self.session = session
        self.special_instruction = special_instruction
        self.status = status
        self.status_description = status_description
        self.stop_price = stop_price
        self.stop_price_link_basis = stop_price_link_basis
        self.stop_price_link_type = stop_price_link_type
        self.stop_price_offset = stop_price_offset
        self.stop_type = stop_type
        self.tag = tag
        self.tax_lot_method = tax_lot_method

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        account_id = from_union([from_int, from_none], obj.get("accountId"))
        activation_price = from_union([from_float, from_none], obj.get("activationPrice"))
        cancelable = from_union([from_bool, from_none], obj.get("cancelable"))
        try:
            cancel_time = from_union([CancelTime.from_dict, from_none], obj.get("cancelTime"))
        except AssertionError:
            cancel_time = obj.get("cancelTime")
        child_order_strategies = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("childOrderStrategies"))
        close_time = from_union([from_datetime, from_none], obj.get("closeTime"))
        complex_order_strategy_type = from_union([ComplexOrderStrategyType, from_none], obj.get("complexOrderStrategyType"))
        destination_link_name = from_union([from_str, from_none], obj.get("destinationLinkName"))
        duration = from_union([Duration, from_none], obj.get("duration"))
        editable = from_union([from_bool, from_none], obj.get("editable"))
        entered_time = from_union([from_datetime, from_none], obj.get("enteredTime"))
        filled_quantity = from_union([from_float, from_none], obj.get("filledQuantity"))
        order_activity_collection = from_union([lambda x: from_list(OrderActivityCollection.from_dict, x), from_none], obj.get("orderActivityCollection"))
        order_id = from_union([from_int, from_none], obj.get("orderId"))
        order_leg_collection = from_union([lambda x: from_list(OrderLegCollection.from_dict, x), from_none], obj.get("orderLegCollection"))
        order_strategy_type = from_union([OrderStrategyType, from_none], obj.get("orderStrategyType"))
        order_type = from_union([OrderType, from_none], obj.get("orderType"))
        price = from_union([from_float, from_none], obj.get("price"))
        price_link_basis = from_union([PriceLinkBasis, from_none], obj.get("priceLinkBasis"))
        price_link_type = from_union([PriceLinkType, from_none], obj.get("priceLinkType"))
        quantity = from_union([from_float, from_none], obj.get("quantity"))
        release_time = from_union([from_datetime, from_none], obj.get("releaseTime"))
        remaining_quantity = from_union([from_float, from_none], obj.get("remainingQuantity"))
        replacing_order_collection = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("replacingOrderCollection"))
        requested_destination = from_union([RequestedDestination, from_none], obj.get("requestedDestination"))
        session = from_union([Session, from_none], obj.get("session"))
        special_instruction = from_union([SpecialInstruction, from_none], obj.get("specialInstruction"))
        status = from_union([Status, from_none], obj.get("status"))
        status_description = from_union([from_str, from_none], obj.get("statusDescription"))
        stop_price = from_union([from_float, from_none], obj.get("stopPrice"))
        stop_price_link_basis = from_union([PriceLinkBasis, from_none], obj.get("stopPriceLinkBasis"))
        stop_price_link_type = from_union([PriceLinkType, from_none], obj.get("stopPriceLinkType"))
        stop_price_offset = from_union([from_float, from_none], obj.get("stopPriceOffset"))
        stop_type = from_union([StopType, from_none], obj.get("stopType"))
        tag = from_union([from_str, from_none], obj.get("tag"))
        tax_lot_method = from_union([TaxLotMethod, from_none], obj.get("taxLotMethod"))
        return OrderStrategy(account_id, activation_price, cancelable, cancel_time, child_order_strategies, close_time, complex_order_strategy_type, destination_link_name, duration, editable, entered_time, filled_quantity, order_activity_collection, order_id, order_leg_collection, order_strategy_type, order_type,
                             price, price_link_basis, price_link_type, quantity, release_time, remaining_quantity, replacing_order_collection, requested_destination, session, special_instruction, status, status_description, stop_price, stop_price_link_basis, stop_price_link_type, stop_price_offset, stop_type, tag, tax_lot_method)

    def to_dict(self):
        result = {}
        result["accountId"] = from_union([from_int, from_none], self.account_id)
        result["activationPrice"] = from_union([to_float, from_none], self.activation_price)
        result["cancelable"] = from_union([from_bool, from_none], self.cancelable)
        result["cancelTime"] = from_union([lambda x: to_class(CancelTime, x), from_none], self.cancel_time)
        result["childOrderStrategies"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.child_order_strategies)
        result["closeTime"] = from_union([lambda x: x.isoformat(), from_none], self.close_time)
        result["complexOrderStrategyType"] = from_union([lambda x: to_enum(ComplexOrderStrategyType, x), from_none], self.complex_order_strategy_type)
        result["destinationLinkName"] = from_union([from_str, from_none], self.destination_link_name)
        result["duration"] = from_union([lambda x: to_enum(Duration, x), from_none], self.duration)
        result["editable"] = from_union([from_bool, from_none], self.editable)
        result["enteredTime"] = from_union([lambda x: x.isoformat(), from_none], self.entered_time)
        result["filledQuantity"] = from_union([to_float, from_none], self.filled_quantity)
        result["orderActivityCollection"] = from_union([lambda x: from_list(lambda x: to_class(OrderActivityCollection, x), x), from_none], self.order_activity_collection)
        result["orderId"] = from_union([from_int, from_none], self.order_id)
        result["orderLegCollection"] = from_union([lambda x: from_list(lambda x: to_class(OrderLegCollection, x), x), from_none], self.order_leg_collection)
        result["orderStrategyType"] = from_union([lambda x: to_enum(OrderStrategyType, x), from_none], self.order_strategy_type)
        result["orderType"] = from_union([lambda x: to_enum(OrderType, x), from_none], self.order_type)
        result["price"] = from_union([to_float, from_none], self.price)
        result["priceLinkBasis"] = from_union([lambda x: to_enum(PriceLinkBasis, x), from_none], self.price_link_basis)
        result["priceLinkType"] = from_union([lambda x: to_enum(PriceLinkType, x), from_none], self.price_link_type)
        result["quantity"] = from_union([to_float, from_none], self.quantity)
        result["releaseTime"] = from_union([lambda x: x.isoformat(), from_none], self.release_time)
        result["remainingQuantity"] = from_union([to_float, from_none], self.remaining_quantity)
        result["replacingOrderCollection"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.replacing_order_collection)
        result["requestedDestination"] = from_union([lambda x: to_enum(RequestedDestination, x), from_none], self.requested_destination)
        result["session"] = from_union([lambda x: to_enum(Session, x), from_none], self.session)
        result["specialInstruction"] = from_union([lambda x: to_enum(SpecialInstruction, x), from_none], self.special_instruction)
        result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        result["statusDescription"] = from_union([from_str, from_none], self.status_description)
        result["stopPrice"] = from_union([to_float, from_none], self.stop_price)
        result["stopPriceLinkBasis"] = from_union([lambda x: to_enum(PriceLinkBasis, x), from_none], self.stop_price_link_basis)
        result["stopPriceLinkType"] = from_union([lambda x: to_enum(PriceLinkType, x), from_none], self.stop_price_link_type)
        result["stopPriceOffset"] = from_union([to_float, from_none], self.stop_price_offset)
        result["stopType"] = from_union([lambda x: to_enum(StopType, x), from_none], self.stop_type)
        result["tag"] = from_union([from_str, from_none], self.tag)
        result["taxLotMethod"] = from_union([lambda x: to_enum(TaxLotMethod, x), from_none], self.tax_lot_method)
        return result


class Position:
    def __init__(self, aged_quantity, average_price, current_day_profit_loss, current_day_profit_loss_percentage,
                 instrument, long_quantity, market_value, settled_long_quantity, settled_short_quantity, short_quantity):
        self.aged_quantity = aged_quantity
        self.average_price = average_price
        self.current_day_profit_loss = current_day_profit_loss
        self.current_day_profit_loss_percentage = current_day_profit_loss_percentage
        self.instrument = instrument
        self.long_quantity = long_quantity
        self.market_value = market_value
        self.settled_long_quantity = settled_long_quantity
        self.settled_short_quantity = settled_short_quantity
        self.short_quantity = short_quantity

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        aged_quantity = from_union([from_float, from_none], obj.get("agedQuantity"))
        average_price = from_union([from_float, from_none], obj.get("averagePrice"))
        current_day_profit_loss = from_union([from_float, from_none], obj.get("currentDayProfitLoss"))
        current_day_profit_loss_percentage = from_union([from_float, from_none], obj.get("currentDayProfitLossPercentage"))
        instrument = from_union([Instrument.from_dict, from_none], obj.get("instrument"))
        long_quantity = from_union([from_float, from_none], obj.get("longQuantity"))
        market_value = from_union([from_float, from_none], obj.get("marketValue"))
        settled_long_quantity = from_union([from_float, from_none], obj.get("settledLongQuantity"))
        settled_short_quantity = from_union([from_float, from_none], obj.get("settledShortQuantity"))
        short_quantity = from_union([from_float, from_none], obj.get("shortQuantity"))
        return Position(aged_quantity, average_price, current_day_profit_loss, current_day_profit_loss_percentage, instrument,
                        long_quantity, market_value, settled_long_quantity, settled_short_quantity, short_quantity)

    def to_dict(self):
        result = {}
        result["agedQuantity"] = from_union([to_float, from_none], self.aged_quantity)
        result["averagePrice"] = from_union([to_float, from_none], self.average_price)
        result["currentDayProfitLoss"] = from_union([to_float, from_none], self.current_day_profit_loss)
        result["currentDayProfitLossPercentage"] = from_union([to_float, from_none], self.current_day_profit_loss_percentage)
        result["instrument"] = from_union([lambda x: to_class(Instrument, x), from_none], self.instrument)
        result["longQuantity"] = from_union([to_float, from_none], self.long_quantity)
        result["marketValue"] = from_union([to_float, from_none], self.market_value)
        result["settledLongQuantity"] = from_union([to_float, from_none], self.settled_long_quantity)
        result["settledShortQuantity"] = from_union([to_float, from_none], self.settled_short_quantity)
        result["shortQuantity"] = from_union([to_float, from_none], self.short_quantity)
        return result


class TypeEnum(Enum):
    CASH = "CASH"
    MARGIN = "MARGIN"


class SecuritiesAccount:
    def __init__(self, account_id, current_balances, is_closing_only_restricted, is_day_trader, order_strategies, positions, round_trips, type):
        self.account_id = account_id
        self.current_balances = current_balances
        self.is_closing_only_restricted = is_closing_only_restricted
        self.is_day_trader = is_day_trader
        self.order_strategies = order_strategies
        self.positions = positions
        self.round_trips = round_trips
        self.type = type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        account_id = from_union([from_str, from_none], obj.get("accountId"))
        current_balances = from_union([CurrentBalances.from_dict, from_none], obj.get("currentBalances"))
        is_closing_only_restricted = from_union([from_bool, from_none], obj.get("isClosingOnlyRestricted"))
        is_day_trader = from_union([from_bool, from_none], obj.get("isDayTrader"))
        order_strategies = from_union([lambda x: from_list(OrderStrategy.from_dict, x), from_none], obj.get("orderStrategies"))
        positions = from_union([lambda x: from_list(Position.from_dict, x), from_none], obj.get("positions"))
        round_trips = from_union([from_int, from_none], obj.get("roundTrips"))
        type = from_union([TypeEnum, from_none], obj.get("type"))
        return SecuritiesAccount(account_id, current_balances, is_closing_only_restricted, is_day_trader, order_strategies, positions, round_trips, type)

    def to_dict(self):
        result = {}
        result["accountId"] = from_union([from_str, from_none], self.account_id)
        result["currentBalances"] = from_union([lambda x: to_class(CurrentBalances, x), from_none], self.current_balances)
        result["isClosingOnlyRestricted"] = from_union([from_bool, from_none], self.is_closing_only_restricted)
        result["isDayTrader"] = from_union([from_bool, from_none], self.is_day_trader)
        result["orderStrategies"] = from_union([lambda x: from_list(lambda x: to_class(OrderStrategy, x), x), from_none], self.order_strategies)
        result["positions"] = from_union([lambda x: from_list(lambda x: to_class(Position, x), x), from_none], self.positions)
        result["roundTrips"] = from_union([from_int, from_none], self.round_trips)
        result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        return result


def accounts_from_dict(s):
    return from_list(SecuritiesAccount.from_dict, s)


def accounts_to_dict(x):
    return from_list(lambda x: to_class(SecuritiesAccount, x), x)
