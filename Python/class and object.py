# from __future__ import print_function


# *CLASSES AND OBJECT
#
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.gender = "male"
#         self.age = age
#
#     def talk(self):
#         print("Hi, I'm", self.name)
#
#     def vote(self):
#         if self.age >= 18:
#             print("I'm eligible to vote.")
#         else:
#             print("I'm not eligible to vote.")
#
#
# name=input("Enter Name: ")
#
# age=int(input("Enter Age: "))
#
# obj = Person(name,age)
# Person.talk (obj)
# obj.vote()

#ENCAPSULATION
class Car:

    def __init__(self,carname,speed):
        self.carname=carname
        self.speed=speed

    def getspeed(self):
        print("Speed of",self.carname ,"is",self.speed)

    def setspeed(self,speed):
        self.speed=speed


class Sedan(Car):

    def accelerate(self,acceleratee):
        self.acceleratee=acceleratee
        print("Speed of",self.carname ,"is",self.speed+self.acceleratee)



bmw=Car("BMW", 154)

bmw.getspeed();

bmw.setspeed(165)

bmw.getspeed();

mah=Sedan("Maruti",120)

mah.getspeed();
mah.accelerate(80)
