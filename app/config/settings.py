import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "database.ini"))

DB_CONFIG = {
  "host": config["DATABASE"]["host"],
  "user": config["DATABASE"]["user"],
  "password": config["DATABASE"]["password"],
  "database": config["DATABASE"]["database"],
  "port": int(config["DATABASE"]["port"])
}