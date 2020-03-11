class User:
    def __init__(self, username, email, plaintext_password, creation_date, last_login_date=None, first_name=None,
                 last_name=None, phone_number=None):
        self.username = username
        self.email = email
        self.password = plaintext_password
        self.creation_date = creation_date
        self.last_login_date = last_login_date
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
