from tests.forms import FakeGeneralSearchForm


class FakeEquipmentSearchForm(FakeGeneralSearchForm):

    def __init__(self, any_field=None, manufacturer=None, name=None, equipment_type=None,
                 description=None):
        super().__init__(any_field)
        self.manufacturer = self.empty_or_data(manufacturer)
        self.name = self.empty_or_data(name)
        self.equipment_type = self.empty_or_data(equipment_type)
        self.description = self.empty_or_data(description)
