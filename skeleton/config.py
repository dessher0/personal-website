from datetime import datetime


class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    OPENAI_API_KEY = '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'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "8473b9c0-5b6c-11eb-ae93-0242ac130002"

    DB_NAME = 'database.db'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///databases/{DB_NAME}'

    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '1d34a45f5cd536'
    MAIL_PASSWORD = '4773809e2a232d'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    #MAIL_SERVER ='smtp.postmarkapp.com'
    #MAIL_PORT = 587
    #MAIL_USERNAME = 'b6430b7f-b2a2-41ee-8648-e2f4cbc05a4a'
    #MAIL_PASSWORD = 'b6430b7f-b2a2-41ee-8648-e2f4cbc05a4a'
    #MAIL_USE_TLS = True
    #MAIL_USE_SSL = False

    CURRENT_YEAR = datetime.now().year


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
