class PracticeCenter:
    def __init__(self, practice_center_id, name, email=None, web_site=None, phone_number=None,
                 climates=None, recommendations=None):
        self.id = practice_center_id
        self.name = name
        self.email = email
        self.web_site = web_site
        self.phone_number = phone_number
        self.climates = [] if climates is None else climates
        self.recommendations = [] if recommendations is None else recommendations

    def __eq__(self, other):
        if isinstance(other, PracticeCenter):
            return self.id == other.id
        return False

    def add_recommendation(self, recommendation):
        self.recommendations.append(recommendation)
