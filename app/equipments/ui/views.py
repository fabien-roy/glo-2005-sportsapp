from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint, flash, url_for, redirect
from flask.views import View
from flask_paginate import get_page_args, Pagination
from injector import inject

from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.forms import EquipmentSearchForm
from app.equipments.repositories import EquipmentRepository

equipment_blueprint = Blueprint('equipments', __name__)


@equipment_blueprint.route('/equipments', methods=('GET', 'POST'))
def equipments(equipment_repository: EquipmentRepository):
    form = EquipmentSearchForm(request.form)
    request_form = form if request.method == 'POST' and form.validate_on_submit() else None

    page, per_page, offset = get_page_args()
    total = equipment_repository.get_count(request_form)
    paged_equipments = equipment_repository.get_all(request_form, offset, per_page)

    pagination = Pagination(page=page, per_page=per_page, total=total, record_name='equipments',
                            format_total=True, format_number=True)
    return render_template('equipments.html', equipments=paged_equipments, page=page,
                           per_page=per_page, pagination=pagination, form=form)


@equipment_blueprint.route('/equipments/<equipment_id>')
def equipment_details(equipment_repository: EquipmentRepository, equipment_id):
    try:
        equipment = equipment_repository.get(int(equipment_id))
    except ValueError:
        return not_found()
    except EquipmentNotFoundException:
        return not_found()

    return render_template('equipment_details.html', equipment=equipment)


def not_found():
    flash('Equipment not found', 'error')
    return redirect(url_for('equipments.equipments'), 303)


class EquipmentView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, equipment_repository: EquipmentRepository):
        self.equipment_repository = equipment_repository
