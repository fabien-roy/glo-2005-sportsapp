from project import db, bcrypt
# from sqlalchemy.ext.hybrid import hybrid_property


class ValidationError(ValueError):
    pass


class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False) # TODO : Use encrypted password
    # _password = db.Column(db.Binary(60), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    telephone = db.Column(db.String(20), nullable=True)
    # creation_date = db.Column(db.DateTime, nullable=False)
    # last_logged_in = db.Column(db.DateTime, nullable=False)

    # recipes = db.relationship('Recipe', backref='user', lazy='dynamic')

    def __init__(self, email, username, plaintext_password, first_name=None, last_name=None, telephone=None):
        self.username = username
        self.email = email
        self.password = plaintext_password
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone

    '''
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def set_password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password)
    '''


class Sport(db.Model):
    __tablename__ = 'sports'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name


class SportRecommendations(db.Model):
    __tablename__ = 'sport_recommendations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    id_sport = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    note = db.Column(db.Integer, nullable=False)

    def __init__(self, username, id_sport, comment, date, note):
        self.username = username
        self.id_sport = id_sport
        self.comment = comment
        self.date = date
        self.note = note


class PracticeCenter(db.Model):
    __tablename__ = 'practice_centers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    web_site = db.Column(db.String(100), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)

    def __init__(self, name, email=None, web_site=None, phone_number=None):
        self.name = name
        self.email = email
        self.web_site = web_site
        self.phone_number = phone_number


class PracticeCenterRecommendations(db.Model):
    __tablename__ = 'practice_center_recommendations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    id_practice_center = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    note = db.Column(db.Integer, nullable=False)

    def __init__(self, username, id_practice_center, comment, date, note):
        self.username = username
        self.id_practice_center = id_practice_center
        self.comment = comment
        self.date = date
        self.note = note


class Climate(db.Model):
    __tablename__ = 'climates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name
