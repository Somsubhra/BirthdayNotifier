import os


class Config:
    def __init__(self):
        pass

    @staticmethod
    def debug():
        return 'OPENSHIFT_PYTHON_IP' not in os.environ

    @staticmethod
    def propagate_exceptions():
        return 'OPENSHIFT_PYTHON_IP' not in os.environ

    @staticmethod
    def secret_key():
        return os.environ.get('SECRET_KEY', '\xfb\x13\xdf\xa1@i\xd6>V\xc0\xbf\x8fp\x16#Z\x0b\x81\xeb\x16')

    @staticmethod
    def host_name():
        return os.environ.get('OPENSHIFT_APP_DNS', 'localhost')

    @staticmethod
    def app_name():
        return os.environ.get('OPENSHIFT_APP_NAME', 'flask')

    @staticmethod
    def ip():
        return os.environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1')

    @staticmethod
    def port():
        return int(os.environ.get('OPENSHIFT_PYTHON_PORT', 5555))

    @staticmethod
    def db_host():
        return os.environ.get('OPENSHIFT_MYSQL_DB_HOST', 'localhost')

    @staticmethod
    def db_user():
        return os.environ.get('OPENSHIFT_MYSQL_DB_USERNAME', 'root')

    @staticmethod
    def db_password():
        return os.environ.get('OPENSHIFT_MYSQL_DB_PASSWORD', 's7a')

    @staticmethod
    def db_name():
        return 'smart'

    @staticmethod
    def db():
        return {
            "host": Config.db_host(),
            "user": Config.db_user(),
            "password": Config.db_password(),
            "name": Config.db_name()
        }

    @staticmethod
    def smtp_server():
        return "smtp.gmail.com"

    @staticmethod
    def smtp_user():
        return "smart.birthday.notifier@gmail.com"

    @staticmethod
    def smtp_password():
        return "%birthdaynotifier%"

    @staticmethod
    def smtp():
        return {
            "server": Config.smtp_server(),
            "user": Config.smtp_user(),
            "password": Config.smtp_password()
        }
