from flask import session

__author__ = "abhishekmadhu"

import uuid
from src.common.database import Database
import datetime
__author__ = "abhishekmadhu"


class Students(object):
    def __init__(self, email, password, institute, guardian_name, student_name, course,
                 created_date, dos, approval_status=None, _id=None):
        self.email = email
        self.password = password
        self.institute = institute
        self.guardian_name = guardian_name
        self.student_name = student_name
        self.course = course
        self._id = _id
        self.created_date = created_date
        self.dos = dos
        self.approval_status = "PENDING" if approval_status is None else approval_status

    def save_to_mongo(self):
        Database.insert(collection='students', data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password,
            'student_name': self.student_name,
            'guardian_name': self.guardian_name,
            'institute': self.institute,
            'created_date': self.created_date,
            'dos': self.dos,
            'course': self.course,
            'approval_status': self.approval_status
        }

    @classmethod
    def from_mongo_by_id(cls, _id):
        # Post.from_mongo('123')
        student_data = Database.find_one(collection='students',
                                         query={'_id': _id})
        return cls(**student_data)

    @classmethod
    def from_mongo_by_email(cls, email):
        data = Database.find_one(collection='students',
                                 query={'email': email})
        if data is not None:
            return cls(**data)
        return None

    @classmethod
    def all_from_mongo(cls):
        data = Database.find(collection='students',
                             query={})
        return cls(**data)

    # this is equivalent to the following --
    # return cls(
    #                    institute=student_data['institute'],
    #                    guardian_name=student_data['guardian_name'],
    #                    student_name=student_data['student_name'],
    #                    created_date=student_data['created_date'],
    #                    course=student_data['course'],
    #                    _id=student_data['_id'])

    # LOGIN RELATED FUNCTIONS   ##############################

    @staticmethod
    def is_login_valid(email, password):
        # User.is_login_valid("abhishekmadhu.uem@gmail.com", "1234")
        student = Students.from_mongo_by_email(email=email)
        if student is not None:
            return student.password == password
        return False

    @classmethod
    def register(cls, email, password, institute, guardian_name, student_name,
                 course, created_date, dos, approval_status, _id):

        student = cls.from_mongo_by_email(email)

        if student is None:
            # student does not exist
            new_student = cls(email, password, institute, guardian_name, student_name,
                              course, created_date, dos, approval_status, _id)
            new_student.save_to_mongo()
            session['email'] = email
            return 1
        else:
            # user exists
            return 0

    @staticmethod
    def login(user_email):
        # if the login credentials above are valid
        # login already valid ie: is_login_valid already called

        session['email'] = user_email

    @staticmethod
    def logout(self):
        session['email'] = None

    def get_details(self):
        return Students.from_mongo_by_id(self._id)    # REFACTORED FUNCTION

    # @staticmethod
    # def using_id(_id):  # blog _id for all posts by one person is same
    #     return [student for student in Database.find(collection='students',
    #                                            query={'_id': _id})]
