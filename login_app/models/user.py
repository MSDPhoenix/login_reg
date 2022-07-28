from login_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_id(cls,data):
        query=  """
                SELECT * FROM users WHERE id=%(id)s;
                """
        result = connectToMySQL('users').query_db(query,data)
        user = cls(result[0])
        return user

    @classmethod
    def get_by_email(cls,data):
        query=  """
                SELECT * FROM users WHERE email=%(email)s;
                """
        result = connectToMySQL('users').query_db(query,data)
        user = cls(result[0])
        return user

    @classmethod
    def get_all(cls):
        query=  """
                SELECT * FROM user;
                """
        result = connectToMySQL('users').query_db(query)
        users = []
        for row in result:
            user = cls(row)
            users.append(user)
        return users

    @classmethod
    def save(cls,data):
        query=  """
                INSERT INTO users   (first_name,last_name,email,password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        return connectToMySQL('users').query_db(query,data)

    @classmethod
    def update(cls,data):
        query=  """
                UPDATE  users 
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,password=%(password)s
                WHERE id = %(user_id)s;
                """
        connectToMySQL('users').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query=  """
                DELETE FROM users WHERE id = %(user_id)s;
                """
        connectToMySQL('users').query_db(query,data)

    @staticmethod
    def validate_register(user):
        is_valid = True
        if len(user['first_name'] < 2):
            flash('xxxx')
            is_valid = False
        if len(user['last_name'] < 2):
            flash('xxxx')
            is_valid = False
        if len(user['password'] < 8):
            flash('xxxx')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('xxxx')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('xxxx')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        # get user by email if email in database
        # if password matches user password

        if len(user['first_name'] < 2):
            flash('xxxx')
            is_valid = False
        if len(user['last_name'] < 2):
            flash('xxxx')
            is_valid = False
        if len(user['password'] < 8):
            flash('xxxx')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('xxxx')
            is_valid = False
        if len(user['password'] < 8):
            flash('xxxx')
            is_valid = False
        return is_valid


