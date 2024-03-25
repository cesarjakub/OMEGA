from src.settings.config_reader import ConfigSettings

def main():
    try:
        data = ConfigSettings.get_database_data()
        print(data[0])
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()