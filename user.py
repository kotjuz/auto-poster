
class User:
    def __init__(self, login, db):
        self.db = db
        self.login = login

        self.password = self.pull_password()
        self.email = self.pull_email()
        self.ID = self.pull_id()

    def pull_password(self):
        return self.db.get_user_password(self.login)

    def pull_email(self):
        return self.db.get_user_email(self.login)

    def pull_id(self):
        return self.db.get_user_id(self.login)

    def pull_all_cars(self):
        return self.db.get_user_cars(self.login)