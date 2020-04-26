import os


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # way to connect to the heroku database
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # local database connection path
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/texts'

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    # folder for storing data
    UPLOAD_TEXT = BASEDIR + '/file/texts/'
