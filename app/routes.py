from app import app, db
from app.models import User
from app.serializers import user_schema, users_schema
from flask import abort, make_response, jsonify, request
from sqlalchemy import or_


@app.route('/')
def index():
    return "Hello World from Flask"


@app.route('/users', methods=['POST'])
def create_user():
    input_data = request.get_json()
    errors = user_schema.validate(input_data)
    if errors:
        abort(make_response(jsonify(error=errors), 404))

    if db.session.query(User).filter(or_(User.username == input_data.get('username'), User.email == input_data.get('email'))).first():
        abort(make_response(jsonify(error="An user exists with this id or email"), 409))

    new_user = user_schema.make_user(input_data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user))


@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    return jsonify(users_schema.dump(all_users))


@app.route('/users/<int:id>', methods=['GET'])
def get_user_detail(id):
    user = User.query.get(id)
    if not user:
        abort(make_response(jsonify(error="User with id {} does not exists".format(id)), 404))

    return jsonify(user_schema.dump(user))


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        abort(make_response(jsonify(error="User with id {} does not exists".format(id)), 404))

    input_data = request.get_json()
    errors = user_schema.validate(input_data)
    if errors:
        abort(make_response(jsonify(error=errors), 404))

    if db.session.query(User).filter(or_(User.username == input_data.get('username'), User.email == input_data.get('email'))).count() > 1:
        abort(make_response(jsonify(error="An user exists with this id or email"), 409))

    user.username = input_data.get('username')
    user.email = input_data.get('email')
    db.session.commit()
    return jsonify(user_schema.dump(user))


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        abort(make_response(jsonify(error="User with id {} does not exists".format(id)), 404))

    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))
