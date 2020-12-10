import json as js
from os import path as file


class Config:
    def __init__(self):
        self.config = self.return_reset_config()

    @staticmethod
    def return_reset_config():
        return {
            "AutoTypeEnabled": False
        }

    def reset_config(self):
        self.config = self.return_reset_config()

    def load_config(self, path: str):
        with open(path, "r") as f:
            self.config = js.load(f)

    def save_config(self, path: str):
        with open(path, "w") as f:
            js.dump(self.config, f)

    @staticmethod
    def create_config(path: str):
        if not file.exists(path):
            open(path, "w+").close()
