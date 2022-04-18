# ANTES:
# class Car:
#     id = int
#     license = str
#     driver = str
#     passenger = str

# DESPUÉS:

from account import Account


class Car:
    id = int
    license = str
    driver = Account("", "")
    passegenger = int

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver
