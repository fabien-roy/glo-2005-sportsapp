class User:
    def __init__(self, email, username, plaintext_password, first_name=None, last_name=None, telephone=None):
        self.username = username
        self.email = email
        self.password = plaintext_password
        self.firstName = first_name
        self.lastName = last_name
        self.telephone = telephone
