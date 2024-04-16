from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.users import Users

class UsersDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Users):
        try:
            msg = "Error with creating user."
            query = """
                    EXEC Add_user ?,?,?,?,?,?
                    """
            params = (record.first_name, record.last_name, record.date_of_birth, record.email, record.phone, record.address, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        msg = "No records."
        try:
            query = """
                    SELECT * FROM User_info
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg

    def update(self, record: Users):
        try:
            msg = "Error with updating user."
            query = """
                    UPDATE users
                    SET First_name = ?, Last_name = ?, Date_of_birth = ?, Email = ?, Phone = ?, Address = ?
                    WHERE ID = ?;
                    """
            params = (record.first_name, record.last_name, record.date_of_birth, record.email, record.phone, record.address, record.id)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Users):
        try:
            msg = "Error with deleting user."
            query = """
                    DELETE FROM users WHERE Email = ?;
                    """
            params = (record.email, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_first(self):
        msg = "No records."
        try:
            query = """
                    SELECT First_name FROM users
                    """
            first = self.database.select(query, msg)
            return first
        except Exception as e:
            return msg

    def read_last(self):
        msg = "No records."
        try:
            query = """
                    SELECT Last_name FROM users
                    """
            last = self.database.select(query, msg)
            return last
        except Exception as e:
            return msg

    def read_record(self):
        msg = "No records."
        try:
            query = """
                    SELECT Email FROM users
                    """
            history = self.database.select(query, msg)
            return history
        except Exception as e:
            return msg
