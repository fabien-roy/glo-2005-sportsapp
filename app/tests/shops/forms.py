from app.tests.forms import FakeForm


class FakeShopsForm(FakeForm):

    def __init__(self, name):
        self.name = self.empty_or_data(name)
