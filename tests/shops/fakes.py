from app.shops.exceptions import ShopNotFoundException
from app.shops.models import Shop

shop1 = Shop(shop_id=1, name='MEC Quebec City', phone_number='418 522-8884',
             web_site='https://www.mec.ca/fr/stores/quebec?utm_medium=organic&utm'
                      'source=google&utm_campaign=my-business-listings&utm_content=quebec')
shop2 = Shop(shop_id=2, name='Sportium', phone_number='418 627-0073',
             web_site='https://www.sportium.ca/fr/nos-magasins/quebec')
shop3 = Shop(shop_id=3, name='Au Grand Bazar La Source Du Sport', phone_number='450 378-2022',
             email='info@grandbazar.ca',
             web_site='https://grandbazar.ca/fr/')


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
