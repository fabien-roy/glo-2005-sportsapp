class Data:

    def __init__(self, data):
        self.data = data


class FakeForm:

    @staticmethod
    def validate_on_submit():
        return True


class FakeSportsForm(FakeForm):

    def __init__(self, name):
        self.name = Data(name)
