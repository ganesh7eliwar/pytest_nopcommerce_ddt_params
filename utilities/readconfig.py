import configparser

config = configparser.RawConfigParser()
config.read("D:\\ct_17_batch_revision\\Pytest_Framework_By_Tushar_Sir\\Pytest_params_DDt\\configuration\\config.ini")


class Readconfig:
    @staticmethod
    def get_email():
        email = config.get('login data', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('login data', 'password')
        return password
