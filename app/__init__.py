from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_bootstrap import Bootstrap

from app.forms import GeneralSearchForm

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

bcrypt = Bcrypt(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
Bootstrap(app)

# Database

import pymysql.cursors


def create_connection():
    return pymysql.connect(host=app.config['MYSQL_HOST'],
                           user=app.config['MYSQL_USER'],
                           password=app.config['MYSQL_PASSWORD'],
                           db=app.config['MYSQL_DB'],
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)


conn = create_connection()

# Blueprints

from app.sports.views import sports_blueprint
from app.practice_centers.views import practice_centers_blueprint
from app.shops.views import shops_blueprint
from app.users.views import users_blueprint

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
def page_bad_request(e):
    return render_template('400.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
