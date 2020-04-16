class Sport:
    def __init__(self, sport_id, name, climates=None, recommendations=None):
        self.id = sport_id
        self.name = name
        self.climates = [] if climates is None else climates
        self.recommendations = [] if recommendations is None else recommendations

    def __eq__(self, other):
        if isinstance(other, Sport):
            return self.id == other.id
        return False

    def add_recommendation(self, recommendation):
        self.recommendations.append(recommendation)
