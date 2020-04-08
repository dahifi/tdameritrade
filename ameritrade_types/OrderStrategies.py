# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = order_strategies_from_dict(json.loads(json_string))


def from_str(x):
    assert isinstance(x, str)
    return x


def from_bool(x):
    assert isinstance(x, bool)
    return x


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class CancelTime:
    def __init__(self, date, short_format):
        self.date = date
        self.short_format = short_format

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        date = from_str(obj.get("date"))
        short_format = from_bool(obj.get("shortFormat"))
        return CancelTime(date, short_format)

    def to_dict(self):
        result = {}
        result["date"] = from_str(self.date)
        result["shortFormat"] = from_bool(self.short_format)
        return result


class ChildOrderStrategy:
    def __init__(self, ):
        pass

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        return ChildOrderStrategy()

    def to_dict(self):
        result = {}
        return result


class OrderLegCollection:
    def __init__(self, order_leg_type, leg_id, instrument, instruction, position_effect, quantity, quantity_type):
        self.order_leg_type = order_leg_type
        self.leg_id = leg_id
        self.instrument = instrument
        self.instruction = instruction
        self.position_effect = position_effect
        self.quantity = quantity
        self.quantity_type = quantity_type

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        order_leg_type = from_str(obj.get("orderLegType"))
        leg_id = from_int(obj.get("legId"))
        instrument = from_str(obj.get("instrument"))
        instruction = from_str(obj.get("instruction"))
        position_effect = from_str(obj.get("positionEffect"))
        quantity = from_int(obj.get("quantity"))
        quantity_type = from_str(obj.get("quantityType"))
        return OrderLegCollection(order_leg_type, leg_id, instrument, instruction, position_effect, quantity, quantity_type)

    def to_dict(self):
        result = {}
        result["orderLegType"] = from_str(self.order_leg_type)
        result["legId"] = from_int(self.leg_id)
        result["instrument"] = from_str(self.instrument)
        result["instruction"] = from_str(self.instruction)
        result["positionEffect"] = from_str(self.position_effect)
        result["quantity"] = from_int(self.quantity)
        result["quantityType"] = from_str(self.quantity_type)
        return result


class OrderStrategy:
    def __init__(self, session, duration, order_type, cancel_time, complex_order_strategy_type, quantity, filled_quantity, remaining_quantity, requested_destination, destination_link_name, release_time, stop_price, stop_price_link_basis, stop_price_link_type, stop_price_offset, stop_type, price_link_basis,
                 price_link_type, price, tax_lot_method, order_leg_collection, activation_price, special_instruction, order_strategy_type, order_id, cancelable, editable, status, entered_time, close_time, tag, account_id, order_activity_collection, replacing_order_collection, child_order_strategies, status_description):
        self.session = session
        self.duration = duration
        self.order_type = order_type
        self.cancel_time = cancel_time
        self.complex_order_strategy_type = complex_order_strategy_type
        self.quantity = quantity
        self.filled_quantity = filled_quantity
        self.remaining_quantity = remaining_quantity
        self.requested_destination = requested_destination
        self.destination_link_name = destination_link_name
        self.release_time = release_time
        self.stop_price = stop_price
        self.stop_price_link_basis = stop_price_link_basis
        self.stop_price_link_type = stop_price_link_type
        self.stop_price_offset = stop_price_offset
        self.stop_type = stop_type
        self.price_link_basis = price_link_basis
        self.price_link_type = price_link_type
        self.price = price
        self.tax_lot_method = tax_lot_method
        self.order_leg_collection = order_leg_collection
        self.activation_price = activation_price
        self.special_instruction = special_instruction
        self.order_strategy_type = order_strategy_type
        self.order_id = order_id
        self.cancelable = cancelable
        self.editable = editable
        self.status = status
        self.entered_time = entered_time
        self.close_time = close_time
        self.tag = tag
        self.account_id = account_id
        self.order_activity_collection = order_activity_collection
        self.replacing_order_collection = replacing_order_collection
        self.child_order_strategies = child_order_strategies
        self.status_description = status_description

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        session = from_str(obj.get("session"))
        duration = from_str(obj.get("duration"))
        order_type = from_str(obj.get("orderType"))
        cancel_time = CancelTime.from_dict(obj.get("cancelTime"))
        complex_order_strategy_type = from_str(obj.get("complexOrderStrategyType"))
        quantity = from_int(obj.get("quantity"))
        filled_quantity = from_int(obj.get("filledQuantity"))
        remaining_quantity = from_int(obj.get("remainingQuantity"))
        requested_destination = from_str(obj.get("requestedDestination"))
        destination_link_name = from_str(obj.get("destinationLinkName"))
        release_time = from_str(obj.get("releaseTime"))
        stop_price = from_int(obj.get("stopPrice"))
        stop_price_link_basis = from_str(obj.get("stopPriceLinkBasis"))
        stop_price_link_type = from_str(obj.get("stopPriceLinkType"))
        stop_price_offset = from_int(obj.get("stopPriceOffset"))
        stop_type = from_str(obj.get("stopType"))
        price_link_basis = from_str(obj.get("priceLinkBasis"))
        price_link_type = from_str(obj.get("priceLinkType"))
        price = from_int(obj.get("price"))
        tax_lot_method = from_str(obj.get("taxLotMethod"))
        order_leg_collection = from_list(OrderLegCollection.from_dict, obj.get("orderLegCollection"))
        activation_price = from_int(obj.get("activationPrice"))
        special_instruction = from_str(obj.get("specialInstruction"))
        order_strategy_type = from_str(obj.get("orderStrategyType"))
        order_id = from_int(obj.get("orderId"))
        cancelable = from_bool(obj.get("cancelable"))
        editable = from_bool(obj.get("editable"))
        status = from_str(obj.get("status"))
        entered_time = from_str(obj.get("enteredTime"))
        close_time = from_str(obj.get("closeTime"))
        tag = from_str(obj.get("tag"))
        account_id = from_int(obj.get("accountId"))
        order_activity_collection = from_list(from_str, obj.get("orderActivityCollection"))
        replacing_order_collection = from_list(ChildOrderStrategy.from_dict, obj.get("replacingOrderCollection"))
        child_order_strategies = from_list(ChildOrderStrategy.from_dict, obj.get("childOrderStrategies"))
        status_description = from_str(obj.get("statusDescription"))
        return OrderStrategy(session, duration, order_type, cancel_time, complex_order_strategy_type, quantity, filled_quantity, remaining_quantity, requested_destination, destination_link_name, release_time, stop_price, stop_price_link_basis, stop_price_link_type, stop_price_offset, stop_type, price_link_basis,
                             price_link_type, price, tax_lot_method, order_leg_collection, activation_price, special_instruction, order_strategy_type, order_id, cancelable, editable, status, entered_time, close_time, tag, account_id, order_activity_collection, replacing_order_collection, child_order_strategies, status_description)

    def to_dict(self):
        result = {}
        result["session"] = from_str(self.session)
        result["duration"] = from_str(self.duration)
        result["orderType"] = from_str(self.order_type)
        result["cancelTime"] = to_class(CancelTime, self.cancel_time)
        result["complexOrderStrategyType"] = from_str(self.complex_order_strategy_type)
        result["quantity"] = from_int(self.quantity)
        result["filledQuantity"] = from_int(self.filled_quantity)
        result["remainingQuantity"] = from_int(self.remaining_quantity)
        result["requestedDestination"] = from_str(self.requested_destination)
        result["destinationLinkName"] = from_str(self.destination_link_name)
        result["releaseTime"] = from_str(self.release_time)
        result["stopPrice"] = from_int(self.stop_price)
        result["stopPriceLinkBasis"] = from_str(self.stop_price_link_basis)
        result["stopPriceLinkType"] = from_str(self.stop_price_link_type)
        result["stopPriceOffset"] = from_int(self.stop_price_offset)
        result["stopType"] = from_str(self.stop_type)
        result["priceLinkBasis"] = from_str(self.price_link_basis)
        result["priceLinkType"] = from_str(self.price_link_type)
        result["price"] = from_int(self.price)
        result["taxLotMethod"] = from_str(self.tax_lot_method)
        result["orderLegCollection"] = from_list(lambda x: to_class(OrderLegCollection, x), self.order_leg_collection)
        result["activationPrice"] = from_int(self.activation_price)
        result["specialInstruction"] = from_str(self.special_instruction)
        result["orderStrategyType"] = from_str(self.order_strategy_type)
        result["orderId"] = from_int(self.order_id)
        result["cancelable"] = from_bool(self.cancelable)
        result["editable"] = from_bool(self.editable)
        result["status"] = from_str(self.status)
        result["enteredTime"] = from_str(self.entered_time)
        result["closeTime"] = from_str(self.close_time)
        result["tag"] = from_str(self.tag)
        result["accountId"] = from_int(self.account_id)
        result["orderActivityCollection"] = from_list(from_str, self.order_activity_collection)
        result["replacingOrderCollection"] = from_list(lambda x: to_class(ChildOrderStrategy, x), self.replacing_order_collection)
        result["childOrderStrategies"] = from_list(lambda x: to_class(ChildOrderStrategy, x), self.child_order_strategies)
        result["statusDescription"] = from_str(self.status_description)
        return result


def order_strategies_from_dict(s):
    return from_list(OrderStrategy.from_dict, s)


def order_strategies_to_dict(x):
    return from_list(lambda x: to_class(OrderStrategy, x), x)
