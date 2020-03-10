class User:
    def __init__(self, email, username, plaintext_password, first_name=None, last_name=None, telephone=None):
        self.username = username
        self.email = email
        self.password = plaintext_password
        self.firstName = first_name
        self.lastName = last_name
        self.telephone = telephone


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
        self.id_sport = sport_id
        self.comment = comment
        self.date = date
        self.note = note


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


class Climate:
    def __init__(self, name):
        self.name = name
