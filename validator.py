import datetime
import re

class Validator():
    @staticmethod
    def validate_title(title):
        pattern = r'^(?=.*[A-Za-zĄąĆćĘęŁłÓóŚśŹźŻż0-9])[A-Za-z0-9ĄąĆćĘęŁłÓóŚśŹźŻż .,!\-]{2,60}$'
        match = re.search(pattern, title)
        if not match:
            return False
        return True

    @staticmethod
    def validate_description(description):
        if len(description) > 2000 or len(description) < 10:
            return False
        return True

    @staticmethod
    def validate_brand(brand):
        if not brand.isalpha() or len(brand) > 15:
            return False
        return True

    @staticmethod
    def validate_body(body):
        possible = ["kombi", "sedan", "hatchback", "coupe", "cabrio", "suv", "inne"]
        if not body.isalpha() or len(body) > 15 or body not in possible:
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
        pattern = r'^(?=.*[A-Za-zĄąĆćĘęŁłÓóŚśŹźŻż0-9])[A-Za-z0-9ĄąĆćĘęŁłÓóŚśŹźŻż .,!\-]{2,25}$'
        match = re.search(pattern, author)
        if not match:
            return False
        return True

    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\-.]+@([\w-]+\.)+[\w-]{2,4}$'
        match = re.search(pattern, email)
        if not match:
            return False
        return True

    @staticmethod
    def validate_phone_number(phone_number):
        pattern = r'[4-8][0-9]{8}'
        match = re.search(pattern, phone_number)
        if not match:
            return False
        return True

    @staticmethod
    def validate_city(city):
        pattern = r'^(?=.*[A-Za-zĄąĆćĘęŁłÓóŚśŹźŻż0-9])[A-Za-z0-9ĄąĆćĘęŁłÓóŚśŹźŻż .,!\-]{2,25}$'
        match = re.search(pattern, city)
        if not match:
            return False
        return True

    @staticmethod
    def validate_vin(vin):
        pattern = r'^[A-HJ-NPR-Z0-9]{17}$'
        match = re.search(pattern, vin)
        if not match:
            return False
        return True

    @staticmethod
    def validate_login(login):
        pattern = r'^[a-zA-Z0-9]{4,20}$'
        match = re.search(pattern, login)
        if not match:
            return False
        return True

    @staticmethod
    def validate_password(password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,20}$'
        match = re.search(pattern, password)
        if not match:
            return False
        return True