class PracticeCenter:
    def __init__(self, practice_center_id, name, email=None, web_site=None, phone_number=None, climates=None):
        self.id = practice_center_id
        self.name = name
        self.email = email
        self.web_site = web_site
        self.phone_number = phone_number
        self.climates = climates

    def __eq__(self, other):
        if isinstance(other, PracticeCenter):
            # TODO : Also check for climates
            return self.id == other.id and self.name == other.name and self.email == other.email and \
                   self.web_site == other.web_site and self.phone_number == other.phone_number
        return False


class PracticeCenterRecommendation:
    def __init__(self, username, practice_center_id, comment, date, note):
        self.username = username
        self.practice_center_id = practice_center_id
        self.comment = comment
        self.date = date
        self.note = note
