from tests.forms import FakeGeneralSearchForm


class FakeSportSearchForm(FakeGeneralSearchForm):

    def __init__(self, any_field=None, name=None, climate=None):
        super().__init__(any_field)
        self.name = self.empty_or_data(name)
        self.climate = self.empty_or_data(climate)
