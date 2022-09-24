from datetime import datetime


class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    OPENAI_API_KEY = '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'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "8473b9c0-5b6c-11eb-ae93-0242ac130002"
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/database.db'
    
    CURRENT_YEAR = datetime.now().year


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}