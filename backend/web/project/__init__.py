from os.path import join, isfile

from flask import Flask
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
if isfile(join('instance', 'flask_full.cfg')):
    app.config.from_pyfile('flask_full.cfg')
else:
    app.config.from_pyfile('flask.cfg')

cors = CORS(app, resources={r"/*": {"origins": "*"}})

# TODO : Remove hello_world route
@app.route('/')
def hello_world():
    return 'Hello World!'
