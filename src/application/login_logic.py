from src.data_access.daos.adminDAO import AdminDAO

class LoginLogic:

    def __init__(self, database):
        self.database = database

    def login(self, email, password, msg):
        try:
            admin = AdminDAO(self.database)
            admin.read_with_params(email, password, msg)
        except Exception as e:
            raise Exception(e)