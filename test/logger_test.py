import unittest
import os
from src.application.event_logger.EventLogger import EventLogger

class TestEventLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_events.log"
        self.logger = EventLogger(self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_event(self):
        # Log some events
        self.logger.log_event("Test info message", "INFO")
        self.logger.log_event("Test warning message", "WARNING")

        self.assertTrue(os.path.exists(self.log_file))

        with open(self.log_file, "r") as file:
            log_content = file.read()
            self.assertIn("INFO", log_content)
            self.assertIn("Test info message", log_content)
            self.assertIn("WARNING", log_content)
            self.assertIn("Test warning message", log_content)

if __name__ == "__main__":
    unittest.main()
