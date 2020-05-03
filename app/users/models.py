class User:
    def __init__(self, username, email, password=None, first_name=None, last_name=None,
                 phone_number=None, creation_date=None, last_login_date=None,
                 sport_recommendations=None, practice_center_recommendations=None):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.creation_date = creation_date
        self.last_login_date = last_login_date
        self.sport_recommendations = [] if sport_recommendations is None else sport_recommendations
        self.practice_center_recommendations = [] if practice_center_recommendations is None else \
            practice_center_recommendations

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False
