from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_cors import CORS

from app.auth.services import login_manager
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

login_manager.init_app(app)

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


# TODO : Move this in an env var
app.secret_key = '90c23021b3e64fcc3418ce8a4fbac4b5441fdebe5d7b93c6451111f2a9fd63c624c0edd5069f' \
                 '01f10aa2aa3d69l7284e357e783f0d40687a1b09de2fb39e2f5b289b584f19d5ee8e6a3a6f37' \
                 '7d275bd4a7fa918bfe3ea03ac5c96f747e09a50fcf777f720e9dadc8fdfb7d1257b92810889a' \
                 'b10999f1dfbcc01df9c47ea35fe4fc35a1d130f69b42b77c6c2ba0591e0b8d8272bd2b5a8aaf' \
                 'd4b2c77c132eacd40e0939a9aed0f292d2e141a6d05fb0221547f5cb49935821238c41fcd55b' \
                 '82bc2be93aa28f13bc9da47adaad46cdd546127ae9d9bc5cdb1e6fe4df01ba2d7e4f4df58884' \
                 'eab71b56029f0fed2ef052fce51cdb919f4d09fbbbc5da2068e30d21c45991059e55623d00d5' \
                 '0c5a8f60f7f409d5a439bfa78aa69dfd77f1c17cfd88cebb6956be5b57666747fe4e98b25c'
