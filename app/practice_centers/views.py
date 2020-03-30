from flask import render_template, Blueprint
from flask.views import View
from injector import inject

from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.repositories import PracticeCentersRepository

practice_centers_blueprint = Blueprint('practice_centers', __name__)


# TODO : Make practice centers query params for search
@practice_centers_blueprint.route('/practice-centers')
def practice_centers(practice_centers_repository: PracticeCentersRepository):
    all_practice_centers = practice_centers_repository.get_all()
    return render_template('practice_centers.html', practice_centers=all_practice_centers)


@practice_centers_blueprint.route('/practice-centers/<practice_center_id>')
def practice_center_details(practice_centers_repository: PracticeCentersRepository, practice_center_id):
    try:
        practice_center = practice_centers_repository.get(practice_center_id)
    except PracticeCenterNotFoundException:
        return render_template('404.html'), 404

    return render_template('practice_center_details.html', practice_center=practice_center)


class PracticeCenterView(View):
    def dispatch_request(self):
        pass

    @inject
    def __init__(self, practice_centers_repository: PracticeCentersRepository):
        self.practice_centers_repository = practice_centers_repository
