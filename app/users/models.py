class User:
    def __init__(self, username, email, first_name=None, last_name=None, phone_number=None, creation_date=None,
                 last_login_date=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.creation_date = creation_date
        self.last_login_date = last_login_date
        # TODO : Add passwords (when making login/register)

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username and self.email == other.email
        return False
