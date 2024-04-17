from datetime import datetime
import os

class EventLogger:

    def __init__(self, path):
        self.path = path

    def log_event(self, message, level):
        try:
            with open(self.path, 'a') as file:
                msg = f"{level} {datetime.now()} | {message}\n"
                file.write(msg)
        except Exception as e:
            print(f"Error with loging {e}")
