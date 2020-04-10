from flask import render_template, request
from flask.views import View
from injector import inject

from app import practice_centers_blueprint
from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.forms import PracticeCentersSearchForm
from app.practice_centers.repositories import PracticeCentersRepository


@practice_centers_blueprint.route('/practice-centers', methods=('GET', 'POST'))
def practice_centers(practice_centers_repository: PracticeCentersRepository):
    form = PracticeCentersSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_practice_centers = practice_centers_repository.get_all(form)
    else:
        all_practice_centers = practice_centers_repository.get_all(None)

    return render_template('practice_centers.html', practice_centers=all_practice_centers,
                           form=form)


@practice_centers_blueprint.route('/practice-centers/<practice_center_id>')
def practice_center_details(practice_centers_repository: PracticeCentersRepository,
                            practice_center_id):
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
