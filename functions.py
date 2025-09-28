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
    def __init__(self, make, model, year, speed):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = speed

    def get_make():
        return self.__make
    def get_model():
        return self.__model
    def get_year():
        return self.__year
    def accelerate():
        self.__speed += 10
        print(f"Accelerating... Current speed: {self.__speed} mph")
    def brake():
        if self.__speed > 0:
            self.__speed -= 10
            print(f"Braking... Current speed is {self.__speed} mph")
        else:
            print("Car Already Stopped")

