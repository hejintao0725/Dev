class Config:
    DEBUG = True
    # mysql+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/student'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # # secret_key
    # SECRET_KEY = 'kdjklfjkd87384hjdhjh'


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DDEBUG = False
