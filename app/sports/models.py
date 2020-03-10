class Sport:
    def __init__(self, sport_id, name):
        self.id = sport_id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Sport):
            return self.id == other.id and self.name == other.name
        return False


class SportRecommendation:
    def __init__(self, username, sport_id, comment, date, note):
        self.username = username
        self.sport_id = sport_id
        self.comment = comment
        self.date = date
        self.note = note
