from app.shops.exceptions import ShopNotFoundException
from instance.shops.fakes import shop1, shop2, shop3

shop1.id = 1
shop2.id = 2
shop3.id = 3


def get_shop(shop_id):
    int_id = int(shop_id)
    if int_id == shop1.id:
        return shop1
    if int_id == shop2.id:
        return shop2
    if int_id == shop3.id:
        return shop3

    return None


def no_shop():
    raise ShopNotFoundException


def get_shops_filtered(form):
    if form is None:
        return [shop1, shop2, shop3]

    return [shop1]
