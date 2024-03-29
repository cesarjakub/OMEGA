from src.data_access.daos.idao import IDao
from src.data_access.database_connection import DatabaseConnection
from src.data_access.tables.admin import Admin


class AdminDAO(IDao):

    def __init__(self, database: DatabaseConnection):
        super().__init__(database)

    def create(self, record: Admin):
        try:
            msg = "Error with creating admin."
            query = """
                    INSERT INTO admin(Users_ID, Role, Password) VALUES(?, ?, ?)
                    """
            params = (record.users_id, record.role, record.password, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read(self):
        try:
            msg = "No records."
            query = """
                    SELECT * FROM admin
                    """
            self.database.select(query, msg)
        except Exception as e:
            raise Exception(e)

    def update(self, record: Admin):
        try:
            msg = "Error with updating admin."
            query = """
                    UPDATE admin SET Users_ID = ?, Role = ?, Password = ? WHERE ID = ?
                    """
            params = (record.users_id, record.role, record.password, record.id, )
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def delete(self, record: Admin):
        try:
            msg = "Error with deleting admin."
            query = """
                    DELETE FROM admin WHERE = Password = ?
                    """
            params = (record.password,)
            self.database.exec(query, params, msg)
        except Exception as e:
            raise Exception(e)

    def read_with_params(self, email, password):
        try:
            msg = "Email or password is wrong! Please try again."
            query = """
                    SELECT Email, Password FROM users INNER JOIN admin ON users.ID = admin.Users_ID 
                    WHERE users.Email = ? AND admin.Password = ?
                    """
            params = (email, password,)
            self.database.select_with_params(query, params, msg)
        except Exception as e:
            raise Exception(e)
