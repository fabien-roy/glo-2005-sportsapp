from flask import render_template, Blueprint

from project.models import Sport

sports_blueprint = Blueprint('sports', __name__)

# TODO : Make sports query params for search
#        Use Sport.query.filter(Sport.x == x, ...).order_by...
@sports_blueprint.route('/sports/')
def sports():
    all_sports = Sport.query.order_by(Sport.name)
    return render_template('sports.html', sports=all_sports)

@sports_blueprint.route('/sports/<sport_id>')
def sport_details(sport_id):
    sport = Sport.query.filter_by(id=sport_id).first_or_404()
    return render_template('sport_details.html', sport=sport)
