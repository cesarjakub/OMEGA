from src.application.logic import Logic
from src.data_access.database_connection import DatabaseConnection

def main():
    database = DatabaseConnection()
    logic = Logic(database)


if __name__ == '__main__':
    main()