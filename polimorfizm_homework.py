# # Task1
# import math
# from math import pi
# class Shape:
    
#     def get_plowad(self):
#         pass


# class Triangle(Shape):
    
#     def __init__(self, a, h):
#         self.a = a
#         self.h = h

#     def get_plowad(self):
#         return float(0.5) * self.a * self.h


# class Square(Shape):
    
#     def __init__(self, C):
#         self.C = C

#     def get_plowad(self):
#         return self.C ** 2

# class Circle(Shape):
    
#     def __init__(self, r):
#         self.r = r

#     def get_plowad(self):
#         return pi * self.r ** 2 

# a1 = Triangle(4, 8)
# a2 = Square(4)
# a3 = Circle(4)

# def get_shape_area():
#     print(a1.get_plowad())
#     print(a2.get_plowad())
#     print(a3.get_plowad())
# get_shape_area()


# # Task2
# class Person:
    
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age

#     @property
#     def age(self):
#         return self.__age 

#     @age.setter
#     def age(self, age):
#         if age in range(1, 130):
#             self.__age = age
#         else:
#             print("Invalid age!")

#     def get_info(self):
#         return f"Hello, my name is {self.name} {self.lastname}"


# class Student(Person):
    
#     def __init__(self, name, lastname, age, university):
#         Person.__init__(self, name, lastname, age)
#         self.university = university

#     def get_info(self):
#         return f"Hello, my name is {self.name} {self.lastname}. I study at {self.university}"

    
# class Employee(Person):

#     def __init__(self, name, lastname, age, company, doljnost):
#         Person.__init__(self, name, lastname, age)
#         self.company = company
#         self.doljnost = doljnost
    
#     def get_info(self):
#         return f"Hello, my name is {self.name} {self.lastname}. I work at: {self.company}, in position: {self.doljnost}"

# a1 = Student('Ivan', 'Erwov', 25, 'Harward')
# a2 = Employee('Sara', 'Keln', 35, 'Facebook', 'programmer')

# def get_human_info():
#     print(a1.get_info())
#     print(a2.get_info())
# get_human_info()


# # Task3
# class MyString:

#     def __init__(self, stroka1, stroka2):
#         self.stroka1 = stroka1
#         self.stroka2 = stroka2
#     def __add__(self):
#         return f"Eto konkatenasia: {self.stroka1 + self.stroka2}"


# class MyInt:
    
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def __add__(self):
#         return f"Eto slojenie: {self.first + self.second}"
 
# a = MyString('my', 'name')
# print(a.__add__())
# b = MyInt(3, 4)
# print(b.__add__())