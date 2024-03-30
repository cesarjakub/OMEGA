from src.presentations.login_scene import LoginScene
from src.application.login_logic import LoginLogic
from src.presentations.main_scene import MainScene

class Logic:

    def __init__(self, database):
        self.database = database
        self.start()

    # login logic
    def start(self):
        login = LoginScene(logic=self)

    def login(self, email, password):
        try:
            login_logic = LoginLogic(self.database)
            login_logic.login(email, password)
        except Exception as e:
            raise Exception(e)

    #main logic
    def main_scene(self):
        main_sc = MainScene(logic=self)