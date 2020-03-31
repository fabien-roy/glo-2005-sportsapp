class Data:

    def __init__(self, data):
        self.data = data


class FakeForm:

    @staticmethod
    def validate_on_submit():
        return True

    @staticmethod
    def empty_or_data(value):
        return Data('') if value is None else Data(value)


class FakeSportsForm(FakeForm):

    def __init__(self, name):
        self.name = self.empty_or_data(name)


class FakePracticeCentersForm(FakeForm):

    def __init__(self, all=None, name=None, email=None, web_site=None, phone_number=None):
        self.all = self.empty_or_data(all)
        self.name = self.empty_or_data(name)
        self.email = self.empty_or_data(email)
        self.web_site = self.empty_or_data(web_site)
        self.phone_number = self.empty_or_data(phone_number)
