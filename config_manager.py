import os.path
import urllib.request, json

from dotenv import load_dotenv
load_dotenv()


class ConfigManager:
    @staticmethod
    def download_config(url):
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            with open("config.json", 'w') as config_file:
                json.dump(data, config_file)

    @staticmethod
    def config_exists(path):
        return os.path.isfile(path)

    @staticmethod
    def load_config(path):
        if not ConfigManager.config_exists(path):
            ConfigManager.download_config(os.getenv("FIRESTORE_KEY_URL"))

    @staticmethod
    def get_config_file():
        CONFIG_FILE = './config.json'
        ConfigManager.load_config(CONFIG_FILE)
        return CONFIG_FILE
