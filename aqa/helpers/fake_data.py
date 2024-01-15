from faker import Faker


class Fake:

    def __init__(self):
        self._fake = Faker()

    def name(self):
        return self._fake.name()

    def email(self):
        return f"{self._fake.first_name()}.{self._fake.last_name()}@intellias"

    def password(self):
        return self._fake.password()

    def text(self):
        return self._fake.text()

    def house_number(self):
        return self._fake.building_number()

    def post_code(self):
        return self._fake.postcode()

    def city(self):
        return self._fake.city()

    def country(self):
        return self._fake.country()

    def street(self):
        return self._fake.street_address()

    def credit_card(self):
        return self._fake.credit_card_number()

    def credit_card_expire(self):
        return self._fake.credit_card_expire()

    def credit_card_cvv(self):
        return  self._fake.credit_card_security_code()