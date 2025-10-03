# def testing(args):
#     print(f"this is a {args}")

# testing("funtion")

##CLASS

# class Dog:
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def bark(self):
#         print(f"{self.__name} says woof!")


# my_dog = Dog("Buddy")

# print(my_dog.get_name())
# my_dog.bark()

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def accelerate(self):
        self.__speed += 10
        print(f"Accelerating... Current speed: {self.__speed} mph")
    def brake(self):
        if self.__speed > 0:
            self.__speed -= 10
            print(f"Braking... Current speed is {self.__speed} mph")
        else:
            print("Car Already Stopped")


# my_car = Car("Toyota", "Camry", 2024)


# print(my_car.get_make())
# print(my_car.get_model())
# print(my_car.get_year())

# my_car.accelerate()
# my_car.accelerate()
# my_car.accelerate()

# my_car.brake()
# my_car.brake()
# my_car.brake()
# my_car.brake()


class House:
    def __init__(self, paint, block, door, bed_room, bath_room, window):
        self.__paint = paint
        self.__block = block
        self.__door = door
        # self.__roof = roof
        self.__bed_room = bed_room
        self.__bath_room = bath_room
        self.__window = window

    def get_blocks(self):
        return self.__block

    def get_paint(self):
        return self.__paint

    def get_doors(self):
        return self.__door

    def get_bedRoom(self):
        return self.__bed_room

    def get_bathRoom(self):
        return self.__bath_room

    def get_window(self):
        return self.__window

    def make_house(self):
        print(f"making house..... just a moment\n")

        print("Finished Building House")


my_house = House("white", 400, 6, 4, 5, 10)

print("Getting Building Materials")
print(f"we are using {my_house.get_blocks()} blocks")
print(f"use {my_house.get_paint()} paint on walls")
print(f"we are using {my_house.get_doors()} doors")''
print(f"the house will have {my_house.get_bedRoom()} bedroom")
print(f"the house will have {my_house.get_bathRoom()} bathroom")
print(f"the house will have {my_house.get_window()} windows")

my_house.make_house()