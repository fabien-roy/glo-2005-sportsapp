from tests.forms import FakeGeneralSearchForm


class FakeEquipmentSearchForm(FakeGeneralSearchForm):

    def __init__(self, any_field=None, manufacturer=None, name=None, category=None,
                 description=None):
        super().__init__(any_field)
        self.manufacturer = self.empty_or_data(manufacturer)
        self.name = self.empty_or_data(name)
        self.category = self.empty_or_data(category)
        self.description = self.empty_or_data(description)
