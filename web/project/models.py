from web.project import db, bcrypt, app
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class ValidationError(ValueError):
    """Class for handling validation errors during
       import of recipe data via API
    """
    pass


class User(db.Model):
    __tablename__ = 'users'

    username = db.column(db.String, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.column(db.String, nullable=False)
    last_name = db.column(db.String, nullable=False)
    first_name = db.column(db.String, nullable=False)
    telephone = db.column(db.String, nullable=False)
    creation_date = db.column(db.DateTime, nullable=False)
    last_logged_in = db.column(db.DateTime, nullable=False)

    # recipes = db.relationship('Recipe', backref='user', lazy='dynamic')

    def __init__(self, email, username, password, last_name, first_name,
                 telephone):
        self.username = username
        self.email = email
        self.password = password
        self.last_name = last_name
        self.first_name = first_name
        self.telephone = telephone



    def import_form_data(self, form):
        """Import the data for this recipe that was input via the EditUserForm
        class.  This can only be done by the administrator.  Additionally, it
        is assumed that the form has already been validated prior to being
        passed in here."""
        try:
            if form.email.data != self.email:
                self.email = form.email.data

            if form.user_role.data != self.role:
                self.role = form.user_role.data

            if form.email_confirmed.data and not self.email_confirmed:
                self.email_confirmed = True
                self.email_confirmed_on = datetime.now()
            elif not form.email_confirmed.data and self.email_confirmed:
                self.email_confirmed = False
                self.email_confirmed_on = None

            if form.new_password.data:
                self.password = form.new_password.data

        except KeyError as e:
            raise ValidationError('Invalid user: missing ' + e.args[0])
        return self

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def set_password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password)

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        """Requires use of Python 3"""
        return str(self.id)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return '<User {}>'.format(self.email)


class Sport(db.Model):
    __tablename__ = 'sports'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name


class SportRecommendations(db.Model):

    __tablename__ = 'sport_recommendations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    id_sport = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=False)
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
    name = db.Column(db.String, nullable=False, unique=True)
    address = db.Column(db.String, nullable=False, unique=True) # TODO : Address must be defined in Location model
    email = db.Column(db.String, nullable=True)
    web_site = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)

    def __init__(self, name, address, email, web_site, phone_number):
        self.name = name
        self.address = address
        self.email = email
        self.web_site = web_site
        self.phone_number = phone_number


class PracticeCenterRecommendations(db.Model):

    __tablename__ = 'practice_center_recommendations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    id_practice_center = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String, nullable=False)
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
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name
