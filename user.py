from database import Database
db = Database()

class User:
    def __init__(self, login):
        self.login = login
        self.password = self.pull_password()
        self.email = self.pull_email()
        self.ID = self.pull_id()

    def pull_password(self):
        return db.get_user_password(self.login)

    def pull_email(self):
        return db.get_user_email(self.login)

    def pull_id(self):
        return db.get_user_id(self.login)