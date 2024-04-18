from datetime import datetime
import os

class EventLogger:
    """A class for logging events to a file."""

    def __init__(self, path):
        """
        Initializes an EventLogger instance.

        Parameters:
            path (str): The path to the log file.
        """
        self.path = path

    def log_event(self, message, level):
        """
        Logs an event message to the specified log file.

        Parameters:
            message (str): The message to be logged.
            level (str): The log level of the message (e.g., 'INFO', 'WARNING', 'ERROR').
        """
        try:
            with open(self.path, 'a') as file:
                msg = f"{level} {datetime.now()} | {message}\n"
                file.write(msg)
        except Exception as e:
            print(f"Error with loging {e}")
