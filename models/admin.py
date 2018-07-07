from flask import session

__author__ = "abhishekmadhu"

import uuid
from common.database import Database
import datetime
__author__ = "abhishekmadhu"


class Admin(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = _id

    def json(self):
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }

    @classmethod
    def from_mongo_by_id(cls, _id):
        # Post.from_mongo('123')
        student_data = Database.find_one(collection='admins',
                                         query={'_id': _id})
        return cls(**student_data)

    @classmethod
    def from_mongo_by_email(cls, email):
        data = Database.find_one(collection='admins',
                                 query={'email': email})
        if data is not None:
            return cls(**data)
        return None

    @staticmethod
    def is_login_valid(email, password):
        # User.is_login_valid("abhishekmadhu.uem@gmail.com", "1234")
        admin = Admin.from_mongo_by_email(email=email)
        if admin is not None:
            return admin.password == password
        return False

    @staticmethod
    def login(user_email):
        # if the login credentials above are valid
        # login already valid ie: is_login_valid already called

        session['email'] = user_email

    @staticmethod
    def logout(self):
        session['email'] = None

    def get_details(self):
        return Admin.from_mongo_by_id(self._id)    # REFACTORED FUNCTION
