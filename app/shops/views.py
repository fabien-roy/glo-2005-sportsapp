from flask import render_template, Blueprint, request
from flask.views import View
from injector import inject

from app.shops.exceptions import ShopNotFoundException
from app.shops.forms import ShopsSearchForm
from app.shops.repositories import ShopsRepository

shops_blueprint = Blueprint('shops', __name__)


@shops_blueprint.route('/shops', methods=('GET', 'POST'))
def shops(shops_repository: ShopsRepository):
    form = ShopsSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_shops = shops_repository.get_all(form)
    else:
        all_shops = shops_repository.get_all(None)

    return render_template('shops.html', shops=all_shops, form=form)


@shops_blueprint.route('/shops/<shop_id>')
def shop_details(shops_repository: ShopsRepository, shop_id):
    try:
        shop = shops_repository.get(shop_id)
    except ShopNotFoundException:
        return render_template('404.html'), 404

    return render_template('shop_details.html', shop=shop)


class ShopView(View):
    def dispatch_request(self):
        pass

    @inject
    def __init__(self, shops_repository: ShopsRepository):
        self.shops_repository = shops_repository