from os.path import join, isfile

from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from web.project.sports.views import sports_blueprint

app = Flask(__name__, instance_relative_config=True)
if isfile(join('instance', 'flask_full.cfg')):
    app.config.from_pyfile('flask_full.cfg')
else:
    app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Blueprints

app.register_blueprint(sports_blueprint)

# Routes

# TODO : Remove hello_world route
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.errorhandler(400)
def page_not_found(e):
    return render_template('400.html'), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
