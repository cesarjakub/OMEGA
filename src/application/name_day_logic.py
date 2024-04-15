import requests

class NameDay:

    def __init__(self, logic, database):
        self.logic = logic
        self.database = database

    def get_name(self):
        api_url = "https://svatkyapi.cz/api/day"

        try:
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:
                return data['name']
            else:
                raise Exception(f"Failed to fetch name day data. Status code: {response.status_code}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
