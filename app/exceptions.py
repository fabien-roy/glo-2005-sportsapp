from app import conn
from app.models import Sport


class SportNotFoundException(Exception):
    pass
