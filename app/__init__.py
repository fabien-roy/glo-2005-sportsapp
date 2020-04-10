from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_bootstrap import Bootstrap

from app.forms import GeneralSearchForm

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

bcrypt = Bcrypt(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
Bootstrap(app)

# Blueprints

sports_blueprint = Blueprint('sports', __name__)
practice_centers_blueprint = Blueprint('practice_centers', __name__)
shops_blueprint = Blueprint('shops', __name__)
users_blueprint = Blueprint('users', __name__)

app.register_blueprint(sports_blueprint)
app.register_blueprint(practice_centers_blueprint)
app.register_blueprint(shops_blueprint)
app.register_blueprint(users_blueprint)


# Routes

@app.route('/')
def home():
    form = GeneralSearchForm(request.form)

    return render_template('index.html', form=form), 200


@app.route('/search', methods=('GET', 'POST'))
def search():
    search_route = request.form.get('search_route')

    return redirect(url_for(search_route), 307)


@app.errorhandler(400)
def page_bad_request():
    return render_template('400.html'), 400


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
