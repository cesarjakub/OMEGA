from src.presentations.login_scene import LoginScene
from src.application.login_logic import LoginLogic
from src.presentations.main_scene import MainScene
from src.presentations.add_book_scene import AddBookScene

class Logic:

    def __init__(self, database):
        self.database = database
        self.main_sc = None
        #self.start()

    # login logic
    def start(self):
        login = LoginScene(logic=self)
        login.mainloop()

    def login(self, email, password):
        try:
            login_logic = LoginLogic(self.database)
            login_logic.login(email, password)
        except Exception as e:
            raise Exception(e)

    #main logic
    def main_scene(self):
        self.main_sc = MainScene(self)
        self.main_sc.mainloop()

    def add_book(self):
        add_book_sc = AddBookScene(self)
        add_book_sc.mainloop()

    def log_out(self):
        self.main_sc.destroy()
        self.start()