from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from codebase.models.student import StudentModel


class Student(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="This can't be blank"
    )
    parser.add_argument(
        'age',
        type=int,
        required=True,
        help="This can't be blank"
    )

    @jwt_required()
    def get(self, name):
        student = StudentModel.find_by_name(name)
        if student:
            return student.json()
        return {"massage": "student not found"}, 404

    def post(self, name):
        if StudentModel.find_by_name(name):
            return {"massage": f"the student called {name} already exists"}, 400

        data = self.parser.parse_args()
        student = StudentModel(name, data["age"])

        try:
            student.save_to_db()
        except(Exception) as e:
            return {"massage": f"An error was occurred: {e}"}, 500
        return student.json(), 201

    def delete(self, name):
        student = StudentModel.find_by_name(name)
        if student:
            StudentModel.delete_from_db(student)
        return {"massage": f"student {name} is deleted"}


class StudentList(Resource):
    def get(self):
        return {"students": [student.json() for student in StudentModel.query.all()]}


