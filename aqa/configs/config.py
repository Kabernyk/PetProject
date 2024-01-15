import os
from os import path

from dotenv import load_dotenv

dotenv_path = path.join(path.dirname(path.dirname(__file__)), ".env")

load_dotenv(dotenv_path)

BASE_URL = "http://localhost/"
SEED_USERNAME = os.getenv("SEED_USERNAME")
SEED_PASSWORD = os.getenv("SEED_PASSWORD")
SEED_FIRSTNAME = os.getenv("SEED_FIRSTNAME")
SEED_LASTNAME = os.getenv("SEES_LASTNAME")
