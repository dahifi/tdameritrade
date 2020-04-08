# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = equity_from_dict(json.loads(json_string))

from .Utils import *


class Instrument:
    def __init__(self, asset_type, cusip, symbol, type=None):
        self.asset_type = asset_type
        self.cusip = cusip
        self.symbol = symbol
        self.type = type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        asset_type = from_str(obj.get("assetType"))
        cusip = from_str(obj.get("cusip"))
        symbol = from_str(obj.get("symbol"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Instrument(asset_type, cusip, symbol, type)

    def to_dict(self):
        result = {}
        result["assetType"] = from_str(self.asset_type)
        result["cusip"] = from_str(self.cusip)
        result["symbol"] = from_str(self.symbol)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


class Position:
    def __init__(self, short_quantity, average_price, current_day_profit_loss, current_day_profit_loss_percentage,
                 long_quantity, settled_long_quantity, settled_short_quantity, instrument, market_value):
        self.short_quantity = short_quantity
        self.average_price = average_price
        self.current_day_profit_loss = current_day_profit_loss
        self.current_day_profit_loss_percentage = current_day_profit_loss_percentage
        self.long_quantity = long_quantity
        self.settled_long_quantity = settled_long_quantity
        self.settled_short_quantity = settled_short_quantity
        self.instrument = instrument
        self.market_value = market_value

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        short_quantity = from_int(obj.get("shortQuantity"))
        average_price = from_float(obj.get("averagePrice"))
        current_day_profit_loss = from_float(obj.get("currentDayProfitLoss"))
        current_day_profit_loss_percentage = from_float(obj.get("currentDayProfitLossPercentage"))
        long_quantity = from_int(obj.get("longQuantity"))
        settled_long_quantity = from_int(obj.get("settledLongQuantity"))
        settled_short_quantity = from_int(obj.get("settledShortQuantity"))
        instrument = Instrument.from_dict(obj.get("instrument"))
        market_value = from_float(obj.get("marketValue"))
        return Position(short_quantity, average_price, current_day_profit_loss, current_day_profit_loss_percentage,
                        long_quantity, settled_long_quantity, settled_short_quantity, instrument, market_value)

    def to_dict(self):
        result = {}
        result["shortQuantity"] = from_int(self.short_quantity)
        result["averagePrice"] = to_float(self.average_price)
        result["currentDayProfitLoss"] = to_float(self.current_day_profit_loss)
        result["currentDayProfitLossPercentage"] = to_float(self.current_day_profit_loss_percentage)
        result["longQuantity"] = from_int(self.long_quantity)
        result["settledLongQuantity"] = from_int(self.settled_long_quantity)
        result["settledShortQuantity"] = from_int(self.settled_short_quantity)
        result["instrument"] = to_class(Instrument, self.instrument)
        result["marketValue"] = to_float(self.market_value)
        return result


class Equity:
    def __init__(self, positions):
        self.positions = positions

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        positions = from_list(Position.from_dict, obj.get("positions"))
        return Equity(positions)

    def to_dict(self):
        result = {}
        result["positions"] = from_list(lambda x: to_class(Position, x), self.positions)
        return result


def equity_from_dict(s):
    return Equity.from_dict(s)


def equity_to_dict(x):
    return to_class(Equity, x)
