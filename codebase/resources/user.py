from codebase.models.usermodel import UserModel
from flask_restful import Resource, reqparse


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This can't be blank"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This can't be blank"
    )

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        user = UserModel(**data)
        try:
            user.save_to_db()
        except(Exception) as e:
            return {"massage": f"An error is occurred: {e}"}, 500

        return {"massage": "user created successfully"}, 201
