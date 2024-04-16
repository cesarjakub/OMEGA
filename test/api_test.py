import unittest
from unittest.mock import patch, MagicMock
from src.application.name_day_logic import NameDay

class TestNameDay(unittest.TestCase):

    @patch('requests.get')
    def test_get_name_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'name': 'John'}

        mock_get.return_value = mock_response

        name_day = NameDay(None, None)
        name = name_day.get_name()

        self.assertEqual(name, 'John')

    @patch('requests.get')
    def test_get_name_failed_request(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404

        mock_get.return_value = mock_response

        name_day = NameDay(None, None)
        with self.assertRaises(Exception) as context:
            name_day.get_name()

        self.assertTrue('Failed to fetch name day data' in str(context.exception))

    @patch('requests.get')
    def test_get_name_exception(self, mock_get):
        mock_get.side_effect = Exception("API Error")

        name_day = NameDay(None, None)
        with self.assertRaises(Exception) as context:
            name_day.get_name()

        self.assertTrue('An error occurred' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
