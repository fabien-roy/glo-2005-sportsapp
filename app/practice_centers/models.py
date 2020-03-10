class PracticeCenter:
    def __init__(self, practice_center_id, name, email=None, web_site=None, phone_number=None):
        self.id = practice_center_id
        self.name = name
        self.email = email
        self.web_site = web_site
        self.phone_number = phone_number


class PracticeCenterRecommendation:
    def __init__(self, username, practice_center_id, comment, date, note):
        self.username = username
        self.practice_center_id = practice_center_id
        self.comment = comment
        self.date = date
        self.note = note
