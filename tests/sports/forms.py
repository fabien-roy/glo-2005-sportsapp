from tests.forms import FakeGeneralSearchForm


class FakeSportsSearchForm(FakeGeneralSearchForm):

    def __init__(self, any_field=None, name=None):
        super().__init__(any_field)
        self.name = self.empty_or_data(name)
