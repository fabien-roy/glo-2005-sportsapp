from flask import render_template, redirect, url_for, request, Blueprint

from app import GeneralSearchForm

root_blueprint = Blueprint('root', __name__)


@root_blueprint.route('/')
def home():
    form = GeneralSearchForm(request.form)

    return render_template('index.html', form=form), 200


@root_blueprint.route('/search', methods=('GET', 'POST'))
def search():
    search_route = request.form.get('search_route')

    return redirect(url_for(search_route), 307)
