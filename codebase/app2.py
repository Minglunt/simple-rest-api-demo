import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from codebase.security import authenticate, identity
from codebase.resources.student import Student
from codebase.resources.user import UserRegister
from codebase.db import db


app = Flask(__name__)
app.secret_key = 'any_password'

api = Api(app)
db.init_app(app)

# security
jwt = JWT(app, authenticate, identity)  # create an /auth endpoint

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(Student, '/student/<string:name>')
api.add_resource(UserRegister, '/registration')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
