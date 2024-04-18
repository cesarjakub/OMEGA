import requests

class NameDay:
    """A class for fetching name day data."""
    def __init__(self, logic, database):
        """
        Initializes a NameDay instance.

        Parameters:
            logic: The logic object associated with name day operations.
            database: The database object used in name day operations.
        """
        self.logic = logic
        self.database = database

    def get_name(self):
        """
        Fetches today's name from an API.

        Returns:
            str: Today's name.

        Raises:
            Exception: If an error occurs during the API request or parsing of the response.
        """
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
