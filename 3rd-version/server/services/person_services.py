from server.databases.util_db import db_util
from server.models import person_models
from server.schemas import person_schemas

def create_person(person_data):
    schema = person_schemas.PersonSchema()
    new_person = person_models.Person(**person_data)
    db_util.session.add(new_person)
    db_util.session.commit()
    print("post:\n",person_data,"\n") # debug
    return schema.dump(new_person)

def get_people():
    people = person_models.Person.query.all()
    schema = person_schemas.PersonSchema(many=True)
    print("get:\n",people,"\n") # debug
    return schema.dump(people)