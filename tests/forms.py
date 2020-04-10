class Data:

    def __init__(self, data):
        self.data = data


class FakeGeneralSearchForm:

    def __init__(self, any_field=None):
        self.any_field = self.empty_or_data(any_field)

    @staticmethod
    def validate_on_submit():
        return True

    @staticmethod
    def empty_or_data(value):
        return Data('') if value is None else Data(value)
