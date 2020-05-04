from tests.forms import FakeForm


class FakeAddRecommendationForm(FakeForm):
    def __init__(self, note, comment):
        self.note = self.empty_or_data(note)
        self.comment = self.empty_or_data(comment)
