from src.presentations.login_scene import LoginScene

class Logic:

    def __init__(self, database):
        self.database = database
        self.start()

    def start(self):
        login = LoginScene(logic=self)
