
from flask import Blueprint, jsonify, request
from server.services import person_services

person_blueprint = Blueprint('person', __name__, url_prefix='/api/people')

@person_blueprint.route('/', methods=['POST'])
def create_person():
    person_data = request.get_json()
    new_person = person_services.create_person(person_data)
    return jsonify(new_person), 201

@person_blueprint.route('/', methods=['GET'])
def get_people():
    people = person_services.get_people()
    return jsonify(people), 200
