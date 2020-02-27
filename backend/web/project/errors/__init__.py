from project import app
from flask import make_response, jsonify

@app.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({'error': 'Bad request', 'message': e.args[0]}), 400)

@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({'error': 'Not found', 'message': e.args[0]}), 404)
