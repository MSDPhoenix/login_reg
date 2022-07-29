from login_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-Z]+$')
db = 'log_registration'

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
        result = connectToMySQL(db).query_db(query,data)
        user = cls(result[0])
        return user

    @classmethod
    def get_by_email(cls,data):
        query=  """
                SELECT * FROM users WHERE email=%(email)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        if len(result)>0:
            user = cls(result[0])
            return user
        return False


    @classmethod
    def get_all(cls):
        query=  """
                SELECT * FROM user;
                """
        result = connectToMySQL(db).query_db(query)
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
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query=  """
                UPDATE  users 
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,password=%(password)s
                WHERE id = %(user_id)s;
                """
        connectToMySQL(db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query=  """
                DELETE FROM users WHERE id = %(user_id)s;
                """
        connectToMySQL(db).query_db(query,data)

    @staticmethod
    def validate_register(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash('First name must be at least 2 characters')
            is_valid = False
        elif not user['first_name'].isalpha():
            flash('First name must contain letters only')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last name must be at least 2 characters')
            is_valid = False
        elif not user['last_name'].isalpha():
            flash('Last name must contain letters only')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must contain at least 8 characters')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('Password does not match confirm password')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Must use valid email format')
            is_valid = False
        if User.get_by_email(user):
            flash('Email address already registered')
            is_valid = False
        return is_valid








    @staticmethod
    def validate_login(user):
        is_valid = True
        # get user by email if email in database
        # if password matches user password

        if len(user['first_name']) < 2:
            flash('First name must be at least 2 characters')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last name must be at least 2 characters')
            is_valid = False
        if not user['first_name'].isalpha():
            flash('First name must contain letters only')
            is_valid = False
        if not user['last_name'].isalpha():
            flash('Last name must contain letters only')
            is_valid = False
        if len(user['password'] < 8):
            flash('Password must contain at least 8 characters')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('Password does not match confirm password')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Must use valid email format')
            is_valid = False
        if len(User.get_by_email(user)) > 0:
            flash('Email address already registered')
            is_valid = False
        return is_valid


