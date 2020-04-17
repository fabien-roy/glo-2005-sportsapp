from tests.forms import FakeGeneralSearchForm


class FakePracticeCenterSearchForm(FakeGeneralSearchForm):

    def __init__(self, any_field=None, name=None, email=None, web_site=None, phone_number=None):
        super().__init__(any_field)
        self.name = self.empty_or_data(name)
        self.email = self.empty_or_data(email)
        self.web_site = self.empty_or_data(web_site)
        self.phone_number = self.empty_or_data(phone_number)
