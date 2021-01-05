from codebase.db import db


class StudentModel(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def json(self):
        return {"name": self.name, "age": self.age}

    @classmethod
    def find_by_name(cls, name) -> 'StudentModel':
        """
        :return: An entity of StudentModel.
        """
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
