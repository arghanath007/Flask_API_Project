import os
from urllib.parse import quote_plus
# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

DB_PASSWORD=quote_plus('arghanath@007')

basedir = os.path.abspath(os.path.dirname(__file__))
SQL_LITE_URI='sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
POSTGRES_DB=f'postgresql://postgres:{DB_PASSWORD}@localhost:5432/DatabaseForAPI'
DB_URI=POSTGRES_DB

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY',  'the_most_well_hidden_secret_key')
    DEBUG=False

class DevelopmentConfig:
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class TestingConfig(Config):
    DEBUG=True
    TESTING=True
    SQLALCHEMY_DATABASE_URI=DB_URI
    PRESERVE_CONTEXT_ON_EXCEPTION=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=DB_URI
    PRESERVE_CONTEXT_ON_EXCEPTION=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base

config_by_name=dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig,
)

key=Config.SECRET_KEY

