from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint, url_for, redirect, flash, session
from flask.views import View
from injector import inject

from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.forms import PracticeCenterSearchForm
from app.practice_centers.repositories import PracticeCenterRepository
from app.recommendations.forms import AddRecommendationForm
from app.recommendations.services import RecommendationService

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


# TODO : Test POST practice_centers.practice_center_details (add recommendation)
@practice_center_blueprint.route('/practice_centers/<practice_center_id>', methods=('GET', 'POST'))
def practice_center_details(practice_centers_repository: PracticeCenterRepository,
                            recommendation_service: RecommendationService, practice_center_id):
    form = AddRecommendationForm(request.form)

    try:
        practice_center = practice_centers_repository.get(practice_center_id)
    except PracticeCenterNotFoundException:
        return render_template('404.html'), 404

    if request.method == 'POST':
        if form.validate_on_submit():
            recommendation_service.add_to_practice_center(session['_user_id'], practice_center,
                                                          form)
            return redirect(url_for('practice_centers.practice_center_details',
                                    practice_center_id=practice_center_id), 302)
        else:
            flash('Error adding recommendation.', 'error')

    return render_template('practice_center_details.html', practice_center=practice_center,
                           form=form)


class PracticeCenterView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, practice_center_repository: PracticeCenterRepository,
                 recommendation_service: RecommendationService):
        self.practice_center_repository = practice_center_repository
        self.recommendation_service = recommendation_service
