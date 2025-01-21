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
        if not fuel.isalpha() or len(fuel) > 20:
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

    