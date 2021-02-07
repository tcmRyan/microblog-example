import os


class Config:
    DEBUG = False
    CSRF_ENABLED = False
    SECRET_KEY = "my-super-secret-key"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = "my-super-secret-dev-key"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:@localhost:5432/blog"
    FLASK_ENV = "development"
