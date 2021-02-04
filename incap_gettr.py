# class Student():

#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     @property
#     def email(self):
#         return f"{self.first}.{self.second}@gmail.com"

#     @property
#     def fullname(self):
#         return f"{self.first} {self.second}"

#     @fullname.setter
#     def fullname(self, name):
#         first, second = name.split(" ")
#         self.first = first
#         self.second = second
    
#     @fullname.deleter
#     def fullname(self):
#         self.first = None
#         self.second = None
#         print('I delete values')


# echo = Student("Echo", "Ewov")
# echo.first = "Alina"
# echo.fullname = "Bakyt Baymatov"

# print(echo.first)
# print(echo.email)
# print(echo.fullname)

# del echo.fullname
# print(echo.second)
# print(echo.fullname)

# class Student():

#     def __init__(self, age):
#         self.__set_age(age)

#     def __get_age(self):
#         return self.__age

#     def __set_age(self, age):
#         if age in list(range(1, 100)):
#             self.__age = age
#         else:
#             print("Invalid age")

#     age = property(__get_age, __set_age)

# student = Student(60)
# print(student.age)
# student = Student(10)
# print(student.age)















































