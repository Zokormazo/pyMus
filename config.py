import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SECRET_KEY = 'vamonos-atamos!'
    WTF_CSRF_ENABLED = False


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db/data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db/data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db/data.sqlite')

    @classmethod
    def init_app(self, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(self, 'MAIL_USERNAME', None) is not None:
            credentials = (self.MAIL_USERNAME, self.MAIL_PASSWORD)
        if getattr(self, 'MAIL_USE_TLS', None):
            secure = ()
        mail_handler = SMTPHandler(
                mailhost=(self.MAIL_SERVER, self.MAIL_PORT),
                fromaddr=self.MAIL_DEFAULT_SENDER,
                toaddrs=[self.ADMINS],
                subject=self.FLASKLLERY_MAIL_SUBJECT_PREFIX + ' Application Error',
                credentials=credentials,
                secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)

config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,

        'default': DevelopmentConfig
}
