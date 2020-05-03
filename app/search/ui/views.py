from flask import render_template, redirect, url_for, request, Blueprint, session

from app.search.forms import GeneralSearchForm

search_blueprint = Blueprint('search', __name__)


@search_blueprint.route('/', methods=('GET', 'POST'))
def search():
    form = GeneralSearchForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        search_route = request.form.get('search_route')
        return redirect(url_for(search_route), 307)

    return render_template('index.html', form=form), 200
