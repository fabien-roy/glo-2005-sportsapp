from abc import ABCMeta, abstractmethod

from flask import Blueprint, render_template
from flask.views import View
from injector import inject

from app.admin.services import StatService

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.route('/admin/stats')
def stats(stat_service: StatService):
    stat_event_sums = stat_service.get_all_stat_event_sums()
    return render_template('stats.html', stats=stat_event_sums)


class AdminView(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dispatch_request(self):
        """ abstract method """

    @inject
    def __init__(self, stat_service: StatService):
        self.stat_service = stat_service
