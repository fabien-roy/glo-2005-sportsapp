from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint, url_for, redirect, flash, session
from flask.views import View
from flask_paginate import get_page_args, Pagination
from injector import inject

from app.practice_centers.exceptions import PracticeCenterNotFoundException
from app.practice_centers.forms import PracticeCenterSearchForm
from app.practice_centers.repositories import PracticeCenterRepository
from app.recommendations.forms import AddRecommendationForm
from app.recommendations.services import RecommendationService

practice_center_blueprint = Blueprint('practice_centers', __name__)


@practice_center_blueprint.route('/practice-centers', methods=('GET', 'POST'))
def practice_centers(practice_center_repository: PracticeCenterRepository):
    form = PracticeCenterSearchForm(request.form)
    request_form = form if request.method == 'POST' and form.validate_on_submit() else None

    page, per_page, offset = get_page_args()
    total = practice_center_repository.get_count(request_form)
    paged_practice_centers = practice_center_repository.get_all(request_form, offset, per_page)

    pagination = Pagination(page=page, per_page=per_page, total=total,
                            record_name='practice centers', format_total=True, format_number=True)
    return render_template('practice_centers.html', practice_centers=paged_practice_centers,
                           page=page, per_page=per_page, pagination=pagination, form=form)


@practice_center_blueprint.route('/practice-centers/<practice_center_id>', methods=('GET', 'POST'))
def practice_center_details(practice_center_repository: PracticeCenterRepository,
                            recommendation_service: RecommendationService, practice_center_id):
    try:
        practice_center = practice_center_repository.get(practice_center_id)
    except PracticeCenterNotFoundException:
        return render_template('404.html'), 404

    form = AddRecommendationForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            recommendation_service.add_to_practice_center(session['_user_id'], practice_center,
                                                          form)
            return redirect(url_for('practice_centers.practice_center_details',
                                    practice_center_id=practice_center_id), 302)

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
