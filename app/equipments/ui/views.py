from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint
from flask.views import View
from injector import inject

from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.forms import EquipmentSearchForm
from app.equipments.repositories import EquipmentRepository

equipment_blueprint = Blueprint('equipments', __name__)


@equipment_blueprint.route('/equipments', methods=('GET', 'POST'))
def equipments(equipments_repository: EquipmentRepository):
    form = EquipmentSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_equipments = equipments_repository.get_all(form)
    else:
        all_equipments = equipments_repository.get_all(None)

    return render_template('equipments.html', equipments=all_equipments, form=form)


@equipment_blueprint.route('/equipments/<equipment_id>')
def equipment_details(equipments_repository: EquipmentRepository, equipment_id):
    try:
        equipment = equipments_repository.get(equipment_id)
    except EquipmentNotFoundException:
        return render_template('404.html'), 404

    return render_template('equipment_details.html', equipment=equipment)


class EquipmentView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, equipment_repository: EquipmentRepository):
        self.equipment_repository = equipment_repository
