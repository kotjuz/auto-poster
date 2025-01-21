import datetime

class Validator():
    @staticmethod
    def validate_title(title):
        if not title.isalpha() or len(title) > 60:
            return False
        return True

    @staticmethod
    def validate_description(description):
        if not description.isalpha() or len(description) > 2000:
            return False
        return True

    @staticmethod
    def validate_brand(brand):
        if not brand.isalpha() or len(brand) > 15:
            return False
        return True

    @staticmethod
    def validate_body(body):
        if not body.isalpha() or len(body) > 15:
            return False
        return True

    @staticmethod
    def validate_fuel(fuel):
        possible = ["diesel", "benzyna", "hybryda", "elektryczny"]
        if not fuel.isalpha() or len(fuel) > 20 or fuel not in possible:
            return False
        return True

    @staticmethod
    def validate_year(year):
        if not year.isdigit() or not (1900 < int(year) < datetime.datetime.now().year + 1):
            return False
        return True

    @staticmethod
    def validate_mileage(mileage):
        if not mileage.isdigit() or not (0 < int(mileage) < 5000000):
            return False
        return True

    @staticmethod
    def validate_engine(engine):
        if not engine.isdigit() or not (40 < int(engine) < 10000):
            return False
        return True

    @staticmethod
    def validate_price(price):
        if not price.isdigit() or not (0 < int(price)):
            return False
        return True

    @staticmethod
    def validate_author(author):
        if not author.isalpha() or not (2 < len(author) < 15):
            return False
        return True