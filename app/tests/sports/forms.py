from app.tests.forms import FakeGeneralSearchForm


class FakeSportsSearchForm(FakeGeneralSearchForm):

    def __init__(self, all=None, name=None):
        super().__init__(all)
        self.name = self.empty_or_data(name)
