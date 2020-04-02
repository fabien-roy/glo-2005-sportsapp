from app.tests.forms import FakeForm


class FakeSportsForm(FakeForm):

    def __init__(self, name):
        self.name = self.empty_or_data(name)
