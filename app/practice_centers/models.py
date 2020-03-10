class PracticeCenter:
    def __init__(self, name, email=None, web_site=None, phone_number=None):
        self.name = name
        self.email = email
        self.web_site = web_site
        self.phone_number = phone_number


class PracticeCenterRecommendation:
    def __init__(self, username, practice_center_id, comment, date, note):
        self.username = username
        self.id_practice_center = practice_center_id
        self.comment = comment
        self.date = date
        self.note = note
