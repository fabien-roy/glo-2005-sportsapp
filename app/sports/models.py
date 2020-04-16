class Sport:
    def __init__(self, sport_id, name, climates=None, recommendations=None):
        if climates is None:
            climates = []

        if recommendations is None:
            recommendations = []

        self.id = sport_id
        self.name = name
        self.climates = climates
        self.recommendations = recommendations

    def __eq__(self, other):
        if isinstance(other, Sport):
            return self.id == other.id
        return False

    def add_recommendation(self, recommendation):
        self.recommendations.append(recommendation)
