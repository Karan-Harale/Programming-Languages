# # Short hand propeerty
#
# # a=3300
# # b=3500
# #
# # print(True) if a < b else print(False)
# #
# #
# # c = (a+b) if a>b else (b - a)if b>a else ""
# # print(c)
#
#
# #enum
#
# # a=[12, 56, 32, 98 ,12 , 45, 1, 4]
# #
# # for index , mark in enumerate(a):
# #     print("Awesome") if index == 3 else print(mark)
#
#
# # Virtual Environment
# '''if 2 peoples uses different versions for coding in that situation how we can use different versions which works same for that perpose we can use virtual environment '''
#
# # import os
# # # os.mkdir("New directory")
# #
# # if(not os.path.exists("New directory")):
# #     os.mkdir("New directory")
# #
# # for i in range(0,100):
# #     os.mkdir(f"New directory/Day {i+1}")
# # #     os.rename(f"New directory/Day {i + 1}", f"New directory/Tutorial {i + 1}")
# #
# #
# # # os.system("cmd")
#
#
# # IO File Handling
#
# # f=open("File1.txt",'w')
# # # f.write("Hello this is file 1")
# # print(f.read())
# # f.close()
#
# # Alternate way
#
# # with open("File1.txt" , 'a') as f:
# #     f.write("\nThis Is alternate method")
#
#
# # '''seek() function changes current position of line in file
# # tell () function return current position of character in file
# #  truncate() is used to remove characters from current byte or character'''
#
# # lambda function
# #
# # def double(x):
# #     return x * 2
# #
# # double = lambda x: x * 2    #both functions goves same output in this lambda function it takes x as argument and return x*2
#
# # print(double(9))
#
#
#
#
# # l = [1,2,3,4,5]
# #
# # newl = list(map(lambda x: x*x*x, l))
# # print(newl)
# #
# #
# # newnewl = list(filter(lambda a: a>10  , newl))
# # print(newnewl)
#
#
# # Reduce function we need to import it from functools
#
# # from functools import reduce
#
# # numbers = [1, 2, 3, 4, 5]
# #
# # # for example if we want to add all the items of numbers without using sum function or for loop we can use reduce method
# #
# # r=reduce(lambda x,y : x*y , numbers) #this will take first two values and return its sum then add that sum to next value until last one
# # print(r)
#
# # Another Best example is factorial of number'
#
# # from functools import reduce
# #
# # number = int(input("Enter number: "))
# #
# # ranges = [i for i in range(1,number+1)]
# #
# # print(ranges)
# #
# # output = reduce(lambda x, y: x*y , ranges)
# #
# # print(f"Factorial of {number} is : {output}")
#
#  # Decorators are used to modifie the code which takes function as an argument and return function
#
#  # e.g
#
# #
# # def greet(fx):
# #
# #  def mfx(*args, **kwargs):
# #   print("Good Morning")
# #   fx( *args, **kwargs)
# #   print("Thank you For using This Function")
# #  return mfx
# #
# #
# # @greet
# # def hello():
# #  print ("Hello World")
# #
# # @greet
# # def add(x,y):
# #  print( x + y )
#
# # hello()
#
# # greet(add(2,3))
#
#
#
# # Getters and setters
#
#
# # class Myclass:
# #
# #     def __init__(self, value):
# #         self._value = value
# #
# #     def display(self):
# #         print(f"Set value is {self._value}")
# #
# #     @property                           #this is getter which made changes and return value
# #     def ten_value(self):
# #         return self._value * 10
# #     #
# #     @ten_value.setter               #this is setter in which we can get value from user and made changes in function
# #
# #     def setval(self, stval):
# #         self._value = stval
# #
# #
# #
# # m1 = Myclass (10)
# # # m1.setval(50)
# # m1.display()
# # print(m1.ten_value)
# #
# # m1.setval = 20
# # m1.display()
# # print(m1.ten_value)
#
#
# # Inheritance
#
#
#
#
# # class Employee:
# #
# #     def __init__(self, name, id):
# #         self.name = name
# #         self.id = id
# #
# #     def showDetails(self):
# #         print(f"The Name of Employee is {self.name} and Employee id is {self.id} ")
# #
# #
# #
# # class Programmer(Employee):   #example of single inheritance
# #     def language(self):
# #         print(f"Default Language is Python")
# #
# #
# #
# #
# # employee1 = Employee("Karan", 101)
# # employee2 = Employee("Rahul", 102)
# #
# # employee1.showDetails()
# # employee2.showDetails()
# #
# #
# # employee3 = Programmer("Akash", 103)
# #
# # employee3.showDetails()
# # employee3.language()
#
#
# '''Multiple Inheritance :- class made up of 2 or more classes
#    mro = Method Resolution Order is used to see from where code starts looking for the methods if methods in two classes are same
#
# '''
#
# # class Employee:  #class 1
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def show(self):
# #         return f"Name of Employee is {self.name}"
# #
# # class danceType:  #class 2
# #     def __init__(self, dancetype):
# #         self.dancetype = dancetype
# #
# #     def show(self):
# #         return f"Dance Type is {self.dancetype}"
# #
# #
# #
# # class dancerEmployee (Employee, danceType):  #Multiple inherited Class
# #
# #     def __init__(self, name, dancetype):
# #         self.name = name
# #         self.dancetype = dancetype
# #
# #
# #
# #
# # e = Employee("xyz")
# # print(e.show())
# #
# # d = danceType("Pop")
# # print(d.show())
# #
# #
# # dancer = dancerEmployee ("abc", "kathak")
# #
# # print(dancer.name)
# # print(dancer.dancetype)
# # print(dancer.show())   #this will return the show function of class Employee because it is written first in inherited class
#
#
#
#
# '''Multilevel Inheritance :- derived class inherits from another derived class
# and it has access to base class
# '''
#
# # class Animal:
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def showDetails(self):
# #         return f"Name : {self.name} \n Age : {self.age}"
# #
# # class Dog(Animal):
# #
# #     def __init__(self, name, age, breed):
# #         Animal.__init__(self,name, age)
# #         self.breed =breed
# #
# #     def showDetails(self):
# #         print(Animal.showDetails(self))
# #         return (f"breed :- {self.breed}")
# #
# # class Husky(Dog):
# #     def __init__(self, name, age, breed, color):
# #         Dog.__init__(self, name, age, breed)
# #         self.color = color
# #
# #     def showDetails(self):
# #         print(Dog.showDetails(self))
# #         return (f"Color :- {self.color}")
# #
# #
# # # a=Animal("Dog",4)
# # #
# # # print(a.showDetails())
# #
# # # b = Dog("Sheru", 4, "Labrodor")
# # #
# # # print(b.showDetails())
# #
# # c = Husky("Smiley", 4, "Husky", "Peark White")
# #
# # print(c.showDetails())
# # print(Husky.mro())
# #
# '''Hybrid inheritance :- In this A deriverd class in created by using 2 or more derived classes
#    hierarchical inheritance:- multiple classes are created by using base class
# '''
#
#
#
# # access specifiers in Pyton
# # -> Access specifier are not available in python although there are conventions to use the access specifiers in python code.
#
# ''' 1) Private specifiers - they are not acceessible either from inside or outside of class. they starts with double underscore(__) and name.(e.g. __name)
#     2) Protected specifiers - they are accessible inside class and from subclasses(child class) (e.g._name)
#     3) Public specifiers - they are accessible from outside of class (e.g. objectname.methodname.variable name.
# '''
#
# # class Employee:
# #
# #     def __init__(self, name):
# #         # self.name = name      #Public access
# #
# #         self._name = name      # Protected Access
# #
# #         self.__name = name    #Private Access
# #
# #     def show(self):
# #         pass
# #
# # e1 = Employee("ABC")
# #
# #
# # # print(e1.name)     # Public access
# #
# # # print(e1._name)    # Protected Access
# #
# # # print(e1.__name)   #Private access  (when we tried to access private member from outside class it gives error in this line.for accessing the private member we can use below method
# #
# # print(e1._Employee__name)  # in this method we start with single underscore classname and then private member name
# #
# # print(e1.__dir__())
#
#
# # when we dont need instant of the class in that case we use static method
#
#
# # class Math:
# #
# #     def __init__(self, num):
# #         self.num = num
# #
# #     def addtonum(self, n):
# #         self.num += n
# #         return self.num
# #
# #
# #     @staticmethod   #in below method we can see in add function self is not used there so if we dont use the static method this function gives us error that we need to use self in it
# #                    #so by using static function we can use same function in class without giving self parameter to it.and call it as normat function .
# #
# #
# #     def add(a, b):
# #         return a+b
# #
# #
# # # m1 = Math.add(2,3)
# # # print(m1)
# #
# # m1 = Math(6)
# # print(m1.num)
# # print(m1.addtonum(5))
# #
# # print(m1.add(6, 4))
# #
#
#
# # Class Method
#
# # class Employee:
# #
# #     company_name = "Apple"
# #
# #     def __init__(self,name):
# #         self.name = name
# #
# #     def show(self):
# #         print(f"The Employee name is {self.name} and works at {self.company_name}")
# #
# #     def changecompany(self, newcompany):  #this function only changes instance variable company
# #         self.company_name = newcompany
# #
# #
# #
# #     @classmethod
# #     def changecompany(self, newcompany):   #this function   changes global or class variable company
# #         self.company_name = newcompany
# #
# #
# #
# # e1 = Employee ("Karan")
# #
# # e1.show()
# #
# # print(f"Before changing the Global company name : {Employee.company_name} \n")
# #
# # e1.changecompany("Tesla")
# # e1.show()
# # print(f"After changing the Global company name : {Employee.company_name} \n")
# #
# #
# #
# # '''in above when we use changecompany function it only changes the company of instance variable that is e1
# # but if we want to change the class method using this function we can use @classmethod
# # so when we made change in change company function it modifiese the company name in class variable which is
# # "Apple" in this case to (Newcompany) in this "Apple" to "tesla"
# # '''
#
# """class method as constructor used when we want to deal with some conjustive code
# when we dont want to code looks like bulky so we use class method in class as constructor which solves the f[problem
# and keeps the bulky part inside the class"""
#
# # class Employee:
# #
# #     def __init__(self, name, salary):
# #         self.name = name
# #         self.salary = salary
# #
# #     @classmethod
# #
# #     def fromstr(cls, strs):
# #         return cls(strs.split("-")[0], strs.split("-")[1])
# #
# #
# #
# # e1=Employee("karan", 12000)
# #
# # print(e1.name)
# # print(e1.salary)
# #
# # '''in aboove scenario the data is given simply like, Employee("Akash", 18000)
# # but if someone gives us data in string format like, str = "Karan-12000" so how can we pass this to our class it gives error
# # if we directly pass it , so there are two ways 1) change in when object declare like e2:
# # '''
# # str1 = "Akash-18000"
# #
# # e2 = Employee(str1.split("-")[0], str1.split("-")[1])
# #
# # print(e2.name)
# # print(e2.salary)
# #
# # '''in above we made changes when object is declared for one employee but we have thousands of
# # entries then same method will make code supphosticated and bulky so we can use effiecient way
# # which is use classmethod as constructor like e3 which makes code more readable'''
# #
# # str3 = "HK-20000"
# #
# # e3 = Employee.fromstr(str3)
# #
# # print(e3.name)
# # print(e3.salary)
#
#
# # dir ,dict and help
#
#
#
# '''Dir :- This method is used to discovering attributes and methods of objects'''
#
# # x = [1,2,3]
#
# # print(x.__dir__())
#
# # print(dir(x))
#
#
# '''Dict :- it returns dictionary of values'''
#
# # class Person():
# #     def __init__(self, name, age ,gender):
# #         self.name = name
# #         self.age = age
# #         self.gender = gender
# #
# #
# # p = Person("karan", 23 ,"M")
# # values = p.__dict__
# #
# # print(values)  #it gives dictionary of values
# #
# # print(f"Keys :- {values.keys()},\nvalues :- {values.values()}")
# #
# #
# # '''Help :- gives all the documentation of class as well as attributes and methods'''
# #
# #
# # print(help(str))
# # print(help(Person))
#
#
# '''Super :- super method is used to access parent class elements in child class
# to avoid repeatation of code
# '''
#
#
#
# # class Parentclass:
# #     def parentmethod(self):
# #         print("This is Parent class method")
# #
# # class Childclass (Parentclass):
# #    def show(self):
# #        print("this is child class method ")
# #        super().parentmethod() # we call show method of child class and use super method to access parent class .
# #
# #
# # childobj1 = Parentclass()
# #
# # childobj2 = Childclass()
# #
# # print(childobj1.parentmethod())
# # print(childobj2.show())
# #
# # # class Parentclass:
# # #     def __init__(self, name, id):
# # #         self.name = name
# # #         self.id = id
# # #
# # # class Childclass (Parentclass):
# # #     def __init__(self,name, id , language):
# # #         # self.name = name      #to avoid this two lines we are using super method by inhereting parentclass and its init method
# # #         # self.id = id
# # #         super().__init__(name, id)
# # #         self.language = language
# # #
# # # childobj1 = Childclass("Karan", 101, "Python")
# # # childobj2 = Childclass("Ravi", 102, "C++")
# # #
# # # print(childobj1.id ," ",childobj1.name," ",childobj1.language)
# # # print(childobj2.id ," ",childobj2.name," ",childobj2.language )
#
# '''method overriding refers to changing the method of parent class in childeclass'''
#
# # class Shape():
# #
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def area(self):
# #         return self.x * self.y
# #
# # class Cirlce(Shape):
# #     def __init__(self, radius):
# #         self.radius = radius
# #
# #         super().__init__(radius,radius)
# #
# #     def area(self):
# #         return 3.14 * super().area()
# #
# # #
# # s1 = Shape(4,4)
# # print(s1.area())
# #
# # c1 = Cirlce (5)
# #
# # print(c1.area())
# #
# # '''in above function we are overloading the area function of class shape to area function of class Circle using super method.'''
#
#
# # exercise- 7 : rename png files
#
# # import os
# #
# # # os.rename("pngs\File1.txt","pngs\extfile1.txt")
# #
# # files = os.listdir("pngs")
# # print(files)
# # p = 1
# #
# # for file in files:
# #     s=file.split(".")
# #     print(s)
# #
# #
# #
# #
# #     if ( s[1] == "jpg"):
# #         # print(f"{s[0]}.png")
# #         # print(file)
# #
# #         os.rename(f"pngs\{file}",f"pngs\png {p}.png")
# #         #
# #         p += 1
# #
# #
#
#
# # operator overloading and dunder methods
#
# # class Vector:
# #
# #     def __init__(self, i, j, k):
# #         self.i = i
# #         self.j = j
# #         self.k = k
# #
# #     def __str__(self):
# #         return f"{self.i}i + {self.j}j + {self.k}k "
# #
# #     # def __add__(self, x):
# #     #     return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k "  # this will return result as string if we want result as a vector quantity then we can use below method
# #
# #
# #     def __add__(self, other):
# #         return Vector(self.i + other.i, self.j + other.j,  self.k + other.k)
# #
# #
# # v1 = Vector(2, 3, 6)
# # v2 = Vector(3, 4, 5)
# #
# #
# # print(v1.__str__())
# # print(v2.__str__())
# #
# #
# # print(Vector.__add__(v1 , v2),"  -: Result")
# #
# # print(type(Vector.__add__(v1 , v2)),"  -: Type")
# #
#
#
# '''walrus operator : it is used to assing the values to variable in expression'''
#
# #without Walrus(:=) operator
#
# # fruits = []
# #
# # while True:
# #     fruit = input("What Fruit do you like :- ")
# #
# #
# #     if fruit == "quit":
# #         break
# #     fruits.append(fruit)
# #
# # print(fruits)
#
# #with Walrus Operator
#
# # fruits = []
# #
# # while (fruit := input("What Fruit do you like :- ")) != "quit":
# #     APlle
# #     fruits.append(fruit)
# #
# # print(fruits)
#
#
# '''Shutil :- used to do os/ computer files operations like rename,copy, move file and folders '''
#
# # import shutil
#
# # shutil.copy("pngs\_firstfile.txt", "pngs\ 1.txt") #Used to make copy of file
#
# # shutil.copytree("./pngs","pngscopy") #used to make copy of folder
#
# # shutil.move("pngs/ 1.txt", "1.txt") #used to move file or folder
#
#
# # shutil.rmtree("./pngscopy") #to remove the folder only
#
#
# # text to Speech
#
# # import win32com.client
# #
# # shoutout = ["Karan","Rahul","Akash","Pote","Hk"]
# #
# # speaker = win32com.client.Dispatch("SAPI.spVoice")
# #
# #
# # for name in shoutout:
# #      speaker.Speak({f"COngratulations {name}"})
#
#
# # Request Parsing
#
# import requests
# # from bs4 import BeautifulSoup
# #
# # responce = requests.get('https://www.google.com/')  #get method used to get htmls
# # # print(responce.text)
# #
# # soup = BeautifulSoup(responce.text, 'html.parser') #beutisoup gives us readable arrangement of html page
# #
# # print(soup)
# #
# # for style in soup.find_all("style"):  #fetching all Style objects of googles link
# #     print(style)
#
#
# # url = 'https://www.w3schools.com/python/demopage.php'
# # myobj = {'somekey': 'somevalue'}
# #
# # x = requests.post(url, json = myobj)  #POST method
# #
# # print(x.text)
#
#
#
# '''Generator : generators does not return naything instead of returning
# they generates the values on the go in a code to avoid use of large memory element
# yeild is used in only generators
# '''
#
#
# # def generator():
# #
# #     for i in range(1000):
# #         yield i
# #
# # gen=generator()
# #
# # # print(next(gen))  #next is used to generate next value we can use for loop for same also.
# # # print(next(gen))
# # # print(next(gen))
# #
# #
# #
# # for j in generator():  #it works same as above
# #     print(next(gen))
# #
# '''Function Caching : is used when we know we want to process definite operations
#  on same values and returns same output so to avoid memory reuses for the same we
#  uses the memoization techniq in which python takes some time to compute
#  the operation 1st time and 2nd time it gives fast results as values are stored in cache so program retrive it from chache itself.
# '''
#
#
# # from functools import lru_cache
# # import time
# #
# # @lru_cache(maxsize=None)
# #
# # def f(x):
# #     time.sleep(5)
# #     return x * 5
# #
# #
# # print("!1st processing...")
# #
# # f(20)
# # print("20 is processed")
# #
# # f(2)
# # print("2 is processed")
# #
# # f(10)
# # print("10 is processed")
# #
# #
# # print("After Preocessing...")
# #
# # f(20)
# # print("20 is processed")
# #
# # f(2)
# # print("2 is processed")
# #
# # f(10)
# # print("10 is processed")
#
# '''Regular Expression'''
#
# # import re
# #
# # # print(dir(re))
# #
# #
# # pattern = 'promote'
# # text = '''The Million Second Quiz is an American game show that was hosted by Ryan Seacrest (pictured) and broadcast by NBC from September 9 to September 19, 2013. For one million seconds, contestants attempted to win trivia matches, and the four top scorers competed in a stepladder playoff for a top prize of $2,000,000. Stephen Lambert, Eli Holzman, and David Hurwitz served as executive producers of The Million Second Quiz. The show helped to promote NBC's lineup for the 2013–14 television season. NBC broadcast a live prime time show for each night of the competition (except during Sunday Night Football), including a two-hour finale. Using a mobile app, viewers could play the game against others and potentially earn a chance to appear as a contestant during the prime time episodes. Critics argued that The Million Second Quiz suffered from a confusing format and a lack of drama. Ratings dropped after the show's premiere.'''
# #
#
#
#
# # searched = re.search(pattern, text)
# #
# # print(searched.span())
# #
# # matched = re.match(pattern, text)
# # print(matched)
# #
# # r = re.split(pattern, text)
# # print(r)
# #
# # print(r[0])
# # print(r[1])
#
# '''Multithreading :
#
# uses of multi threading
#
# 1) when we want download resources parallely  from internet
# 2)
#
# '''
#
# # import time
# # import threading
# # from concurrent.futures import ThreadPoolExecutor
# #
# # def fun(sec):
# #     print(f"Function is runniing for {sec} second")
# #     time.sleep(sec)
# #     return sec
#
# '''in below method one file start downloading after another'''
# # print(fun(3))
# # print(fun(2))
# # print(fun(1))
#
# '''instead of this we can use threading method for downloading the files at same time '''
# # def main():
# #     t1 = threading.Thread(target=fun , args=[3])
# #     t2 = threading.Thread(target=fun , args=[2])
# #     t3 = threading.Thread(target=fun , args=[1])
# #
# #     t1.start()
# #     t2.start()
# #     t3.start()
# #
# #     t1.join()   # waits to complete first opearation then takes next
# #     t2.join()
# #     t3.join()
#
#
#
#
# # def poolingDemo():
# #     with ThreadPoolExecutor() as executor:
# #
# #         # method 1
# #
# #         f1 = executor.submit(fun, 5)
# #         f2 = executor.submit(fun, 4)
# #         f3 = executor.submit(fun, 3)
# #
# #         print(f1.result())
# #
# #         # method 2 using map function most efficient way
# #         l = [2, 3, 4, 6]
# #
# #         results = executor.map(fun, l)
# #
# #         for result in results:
# #             print(result)
# #
# #
# # poolingDemo()
#
#
#
# '''Multiprocessing '''
#
#
# import multiprocessing
# import requests
#
# # def downloadFile(url, name):
#
#     print(f"Started Downloading file {name}")
#
#     responce = requests.get(url)
#     open(f"Files/file{name}.jpg", "wb").write(responce.content)
#     print(f"file {name} download finished")
# #
# #
# # url  = "https://picsum.photos/200/300"
# #
# # for i in range(5):  #download random 5 images from above url
# #     downloadFile(url, i)
# #
#
# # To download files at same time
#
# import requests
# import multiprocessing
# from concurrent.futures import ProcessPoolExecutor
#
#
# def downloadFile(url, name):
#
#     print(f"Started Downloading file {name}")
#
#     responce = requests.get(url)
#     open(f"Files/file {name}.jpg", "wb").write(responce.content)
#     print(f"file {name} download finished")
#
#
#
# if __name__ == '__main__':
#     url  = "https://picsum.photos/200/300"
#
#     processes = []
#
#     '''Method 1'''

    # for i in range(50):  #download random 50 images from above url using multiprocessing
    #
    #     # '''Method 1'''
    #     p = multiprocessing.Process(target= downloadFile, args = [url,i])
    #     p.start()
    #     processes.append(p)
    #
    # print(processes)
    #
    # for process in processes:
    #     process.join()

    # '''Method 2'''
    # with ProcessPoolExecutor() as p:
    #     u = [url for u in range(50)]
    #     l = [i for i in range(50)]
    #
    #     results = p.map(downloadFile, u, l)
    #
    #     for result in results:
    #         print(result)




from tkinter import *
from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
#


# import tkinter as tk
#
# class App(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack()
#
#         self.entrythingy = tk.Entry()
#         self.entrythingy.pack()
#
#         # Create the application variable.
#         self.contents = tk.StringVar()
#         # Set it to some value.
#         self.contents.set("this is a variable")
#         # Tell the entry widget to watch this variable.
#         self.entrythingy["textvariable"] = self.contents
#
#         # Define a callback for when the user hits return.
#         # It prints the current value of the variable.
#         self.entrythingy.bind('<Key-Return>',
#                              self.print_contents)
#
#     def print_contents(self, event):
#         print("Hi. The current entry content is:",
#               self.contents.get())
#
# root = tk.Tk()
# myapp = App(root)
# myapp.mainloop()


