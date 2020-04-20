from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint
from flask.views import View
from injector import inject

from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.forms import PracticeCenterSearchForm
from app.practice_centers.repositories import PracticeCenterRepository

practice_center_blueprint = Blueprint('practice_centers', __name__)


@practice_center_blueprint.route('/practice-centers', methods=('GET', 'POST'))
def practice_centers(practice_centers_repository: PracticeCenterRepository):
    form = PracticeCenterSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_practice_centers = practice_centers_repository.get_all(form)
    else:
        all_practice_centers = practice_centers_repository.get_all(None)

    return render_template('practice_centers.html', practice_centers=all_practice_centers,
                           form=form)


@practice_center_blueprint.route('/practice-centers/<practice_center_id>')
def practice_center_details(practice_centers_repository: PracticeCenterRepository,
                            practice_center_id):
    try:
        practice_center = practice_centers_repository.get(practice_center_id)
    except PracticeCenterNotFoundException:
        return render_template('404.html'), 404

    return render_template('practice_center_details.html', practice_center=practice_center)


class PracticeCenterView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, practice_center_repository: PracticeCenterRepository):
        self.practice_center_repository = practice_center_repository
