
def get_all(Model, Serializer):
    serializer = Serializer(many=True)
    _objects = Model.query.all()
    result = serializer.dump(_objects)
    return result


def calculate_order_price(order, ingredients):

    size_price = order.size.price
    ingredients_price = sum(ingredient.price for ingredient in ingredients)
    total_price = size_price + ingredients_price
    return round(total_price, 2)


def check_required_keys(keys: tuple, _element: dict):
    return all(_element.get(key) for key in keys)
