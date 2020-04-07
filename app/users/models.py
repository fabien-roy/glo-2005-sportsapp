class User:
    def __init__(self, username, email, first_name=None, last_name=None, phone_number=None, creation_date=None,
                 last_login_date=None, sport_recommendations=None, practice_center_recommendations=None):
        if sport_recommendations is None:
            sport_recommendations = []

        if practice_center_recommendations is None:
            practice_center_recommendations = []

        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.creation_date = creation_date
        self.last_login_date = last_login_date
        self.sport_recommendations = sport_recommendations
        self.practice_center_recommendations = practice_center_recommendations

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username and self.email == other.email
        return False

    def add_sport_recommendation(self, sport_recommendation):
        self.sport_recommendations.append(sport_recommendation)

    def add_practice_center_recommendation(self, practice_center_recommendation):
        self.practice_center_recommendations.append(practice_center_recommendation)
