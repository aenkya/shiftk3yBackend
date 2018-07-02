""" Contains App's Configurations """

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
    """ Base Config Model to be inherited by other configuration envs """

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    BASE_DIR = os.path.dirname(__file__)
    PAGE_LIMIT = 10
    DEFAULT_PAGE = 1
    PUBLIC_KEY = os.environ.get('PUBLIC_KEY')

class Development(Config):
    """ Model for Development Environment Config Object """
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Testing(Config):
    """ Model for Testing Environment Config Object """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PUBLIC_KEY = os.environ.get('PUBLIC_KEY_TEST')
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE') or \
        "sqlite:///" + Config.BASE_DIR + "/dev_db.sqlite"

class Staging(Development):
    """Model Staging enviroment config object."""

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

configuration = {
    "Testing": Testing,
    "Development": Development,
    "Production": Config,
    "Staging": Staging
}
