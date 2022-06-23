# Defining Car class
class Car:

    # Initialize class attributes of the class
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Defining class methods
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


# Creating a Car object
my_car = Car("2022 Trailblazer", "Chevy")

# Using "for" loops to run the methods 5x
for i in range(5):
    my_car.accelerate()
    print(my_car.get_speed())

for i in range(5):
    my_car.brake()
    print(my_car.get_speed())
