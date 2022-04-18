
# ANTES:

# from car import Car

# if __name__ == "__main__":
#     print("Hola, Mundo!")
#     car = Car()
#     car.license = "AMS234"
#     car.driver = "Andrés Herrera"
#     print(vars(car))

#     car2 = Car()
#     car2.license = "QWE567"
#     car2.driver = "Martha Herrera"
#     print(vars(car2))

# DESPUÉS:

from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")

    car = Car("AMS234", Account("Andrés Herrera", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))
