from flask import Flask, jsonify, request
from config import app, db
from model import User, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()

@app.route('/', methods=['GET'])
def get_user():
    user_all = User.query.all()
    output = users_schema.dump(user_all)
    print(output)
    return jsonify(output)


@app.route('/create', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username, email)
    db.session.add(new_user)
    db.session.commit()
    return ('user created sucessfully')


@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return(user_schema.jsonify(user))


@app.route("/update/<id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    user.email = request.json['email']
    user.username = request.json['username']
    db.session.commit()
    return('user updated sucessfully')


@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    user_delete = User.query.get(id)
    db.session.delete(user_delete)
    db.session.commit()
    return('user deleted sucessfully')
