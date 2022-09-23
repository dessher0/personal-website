from datetime import datetime

CURRENT_YEAR = datetime.now().year
OPENAI_API_KEY = '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'


class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "8473b9c0-5b6c-11eb-ae93-0242ac130002"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}