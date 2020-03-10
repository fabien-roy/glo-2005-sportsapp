from app.users.repositories import UserRepository


class MySQLUserRepository(UserRepository):
    table_name = 'users'

    username_col = 'username'
    email_col = 'email'
    password_col = 'password'  # TODO : Move password to another table
    first_name_col = 'first_name'
    last_name_col = 'last_name'
    telephone_col = 'telephone'

    # TODO : Rest of UserQuery
