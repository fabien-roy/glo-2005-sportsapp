from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint, url_for, redirect, flash
from flask.views import View
from flask_paginate import get_page_args, Pagination
from injector import inject

from app.shops.exceptions import ShopNotFoundException
from app.shops.forms import ShopSearchForm
from app.shops.repositories import ShopRepository

shop_blueprint = Blueprint('shops', __name__)


@shop_blueprint.route('/shops', methods=('GET', 'POST'))
def shops(shop_repository: ShopRepository):
    form = ShopSearchForm(request.form)
    request_form = form if request.method == 'POST' and form.validate_on_submit() else None

    page, per_page, offset = get_page_args()
    total = shop_repository.get_count(request_form)
    paged_shops = shop_repository.get_all(request_form, offset, per_page)

    pagination = Pagination(page=page, per_page=per_page, total=total, record_name='shops',
                            format_total=True, format_number=True)
    return render_template('shops.html', shops=paged_shops, page=page, per_page=per_page,
                           pagination=pagination, form=form)


@shop_blueprint.route('/shops/<shop_id>')
def shop_details(shop_repository: ShopRepository, shop_id):
    try:
        shop = shop_repository.get(int(shop_id))
    except ValueError:
        return not_found()
    except ShopNotFoundException:
        return not_found()

    return render_template('shop_details.html', shop=shop)


def not_found():
    flash('Shop not found', 'error')
    return redirect(url_for('shops.shops'), 303)


class ShopView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, shop_repository: ShopRepository):
        self.shop_repository = shop_repository
