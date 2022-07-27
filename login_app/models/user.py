from login_app.config.mysqlconnection import connectToMySQL


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
    def get_one(cls,data):
        query=  """
                SELECT * FROM users WHERE id=%(id)s;
                """
        result = connectToMySQL('users').query_db(query,data)
        user = cls(result[0])
        return user

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

    def save(cls,data):
        query=  """
                INSERT INTO users   (first_name,last_name,email,password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        return connectToMySQL('users').query_db(query,data)

    def update(cls,data):
        query=  """
                UPDATE  users 
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,password=%(password)s
                WHERE id = %(user_id)s;
                """
        connectToMySQL('users').query_db(query,data)

    def delete(cls,data):
        query=  """
                DELETE FROM users WHERE id = %(user_id)s;
                """
        connectToMySQL('users').query_db(query,data)

    # def xxx(cls,data):
    #     query=  """

    #             """
    #     result = connectToMySQL('users').query_db(query,data)
    #     return xxxx


