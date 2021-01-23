import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #'839c91f955762c458c526e67f90a0a68'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


