from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint
from flask.views import View
from injector import inject

from app.shops.exceptions import ShopNotFoundException
from app.shops.forms import ShopSearchForm
from app.shops.repositories import ShopRepository

shop_blueprint = Blueprint('shops', __name__)


@shop_blueprint.route('/shops', methods=('GET', 'POST'))
def shops(shops_repository: ShopRepository):
    form = ShopSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_shops = shops_repository.get_all(form)
    else:
        all_shops = shops_repository.get_all(None)

    return render_template('shops.html', shops=all_shops, form=form)


@shop_blueprint.route('/shops/<shop_id>')
def shop_details(shops_repository: ShopRepository, shop_id):
    try:
        shop = shops_repository.get(shop_id)
    except ShopNotFoundException:
        return render_template('404.html'), 404

    return render_template('shop_details.html', shop=shop)


class ShopView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, shop_repository: ShopRepository):
        self.shop_repository = shop_repository
