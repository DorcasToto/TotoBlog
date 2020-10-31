import os

class Config:

    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}