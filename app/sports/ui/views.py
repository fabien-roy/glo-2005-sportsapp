from abc import abstractmethod, ABCMeta

from flask import render_template, request, Blueprint, session
from flask.views import View
from injector import inject

from app.recommendations.forms import AddRecommendationForm
from app.recommendations.services import RecommendationService
from app.sports.exceptions import SportNotFoundException
from app.sports.forms import SportSearchForm
from app.sports.repositories import SportRepository

sport_blueprint = Blueprint('sports', __name__)


@sport_blueprint.route('/sports', methods=('GET', 'POST'))
def sports(sports_repository: SportRepository):
    form = SportSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        all_sports = sports_repository.get_all(form)
    else:
        all_sports = sports_repository.get_all(None)

    return render_template('sports.html', sports=all_sports, form=form)


# TODO : Test POST sports.sport_details (add recommendation)
@sport_blueprint.route('/sports/<sport_id>', methods=('GET', 'POST'))
def sport_details(sports_repository: SportRepository,
                  recommendation_service: RecommendationService, sport_id):
    try:
        sport = sports_repository.get(sport_id)
    except SportNotFoundException:
        return render_template('404.html'), 404

    if request.method == 'POST':
        form = AddRecommendationForm(request.form)
        if form.validate_on_submit():
            recommendation_service.add_to_sport(session['user_id'], sport, form)

    return render_template('sport_details.html', sport=sport)


class SportView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, sport_repository: SportRepository,
                 recommendation_service: RecommendationService):
        self.sport_repository = sport_repository
        self.recommendation_service = recommendation_service
