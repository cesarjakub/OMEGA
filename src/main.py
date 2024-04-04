from src.application.logic import Logic
from src.data_access.database_connection import (DatabaseConnection)
from src.presentations.main_scene import MainScene

def main():
    database = DatabaseConnection()
    logic = Logic(database)
    logic.main_scene()


if __name__ == '__main__':
    main()