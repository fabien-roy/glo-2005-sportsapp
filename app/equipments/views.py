from flask import render_template, request, Blueprint
from flask.views import View
from injector import inject

from app.equipments.exceptions import EquipmentNotFoundException
from app.equipments.forms import EquipmentsSearchForm
from app.equipments.repositories import EquipmentsRepository

equipments_blueprint = Blueprint('equipments', __name__)


@equipments_blueprint.route('/equipments', methods=('GET', 'POST'))
def equipments(equipments_repository: EquipmentsRepository):
    form = EquipmentsSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_equipments = equipments_repository.get_all(form)
    else:
        all_equipments = equipments_repository.get_all(None)

    return render_template('equipments.html', equipments=all_equipments,
                           form=form)


@equipments_blueprint.route('/equipments/<equipment_id>')
def equipment_details(equipments_repository: EquipmentsRepository, equipment_id):
    try:
        equipment = equipments_repository.get(equipment_id)
    except EquipmentNotFoundException:
        return render_template('404.html'), 404

    return render_template('equipment_details.html', equipment=equipment)


class EquipmentView(View):
    def dispatch_request(self):
        pass

    @inject
    def __init__(self, equipments_repository: EquipmentsRepository):
        self.equipments_repository = equipments_repository
