from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_cors import CORS

# from app.auth.services import login_manager
from app.admin.ui.views import admin_blueprint
from app.auth.ui.views import auth_blueprint
from app.equipments.ui.views import equipment_blueprint
from app.practice_centers.ui.views import practice_center_blueprint
from app.search.ui.views import search_blueprint
from app.shops.ui.views import shop_blueprint
from app.sports.ui.views import sport_blueprint
from app.users.ui.views import user_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

bcrypt = Bcrypt(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
Bootstrap(app)


app.register_blueprint(admin_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(sport_blueprint)
app.register_blueprint(practice_center_blueprint)
app.register_blueprint(shop_blueprint)
app.register_blueprint(equipment_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(auth_blueprint)


@app.errorhandler(400)
def page_bad_request():
    return render_template('400.html'), 400


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
