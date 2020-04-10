class Recommendation:
    def __init__(self, recommendation_id, item_id, username, comment, note, name, date=None):
        self.id = recommendation_id
        self.item_id = item_id
        self.username = username
        self.comment = comment
        self.note = note
        self.name = name
        self.date = date

    def __eq__(self, other):
        if isinstance(other, Recommendation):
            return self.id == other.id and self.username == other.username and self.comment == \
                   other.comment and self.note == other.note and self.name == other.name
        return False
