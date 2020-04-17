from tests.forms import FakeGeneralSearchForm


class FakeEquipmentSearchForm(FakeGeneralSearchForm):

    def __init__(self, any_field=None, name=None, category=None, description=None):
        super().__init__(any_field)
        self.name = self.empty_or_data(name)
        self.category = self.empty_or_data(category)
        self.description = self.empty_or_data(description)
