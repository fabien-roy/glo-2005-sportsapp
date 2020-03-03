from project import app
from project.models import ValidationError
from flask import make_response, jsonify

@app.errorhandler(ValidationError)
def general_error(e):
    return bad_request(e)

@app.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({'error': 'Bad request', 'message': e.args[0]}), 400)

@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({'error': 'Not found', 'message': e.args[0]}), 404)
