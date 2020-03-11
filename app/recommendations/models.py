class Recommendation:
    def __init__(self, recommendation_id, username, comment, note, date=None):
        self.id = recommendation_id
        self.username = username
        self.comment = comment
        self.note = note
        self.date = date
