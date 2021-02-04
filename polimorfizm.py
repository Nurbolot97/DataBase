# class Car:
#     def start(self, a, b=None):
#         if b is not None:
#             print(a+b)
#         else:
#             print(a)

# car = Car()
# car.start(10)
# car.start(10, 20)



# class Country():
#     def capital(self):
#         pass

#     def language(self):
#         pass

#     def type_(self):
#         pass


# class Kyrgyzstan(Country):
#     def capital(self):
#         print("Bishkek is the capital of KR")

#     def language(self):
#         print("Kyrgyz is primary language of KR")

#     def type_(self):
#         print("Kyrgyzstan is country with presidental country")


# class Russia(Country):
#     def capital(self):
#         print("Moscow is the capital of Rf")

#     def language(self):
#         print("Russian is primary language of RF")

#     def type_(self):
#         print("RF is country with presidental country")


# class USA(Country):
#     def capital(self):
#         print("Vashington is the capital of USA")

#     def language(self):
#         print("English is primary language of USA")

#     def type_(self):
#         print("USA is country with presidental country")

# obj_kg = Kyrgyzstan()
# obj_russ = Russia()
# obj_usa = USA()

# for country in (obj_kg, obj_russ, obj_usa):
#     country.capital()
#     country.language()
#     country.type_()
#     print()


# class Shape():
#     """
#     This is a parent class that indentent to be inherited by other class
#     """
#     def calculate_area(self):
#         """
#         This is the notebook
#         """
#         raise NotImplementedError


# class Square(Shape):
#     """
#     This is the subclass of Shape class
#     """
#     side_lenght = 2

#     def calculate_area(self):
#         """
#         This is override of parent class method Shape.calculate_area()
#         """
#         return self.side_lenght ** 2

        
# class Triangle(Shape):
#     """
#     This is the subclass of Shape class
#     """
#     base_length = 4
#     height = 3
#     a.get_login
#     def calculate_area(self):
#         """
#         This is override of parent class method Shape.calculate_area()
#         """
#         return self.base_length * self.height * 0.5

# obj_square = Square()
# obj_triangle = Triangle()

# print(obj_square.calculate_area())
# print(obj_triangle.calculate_area())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Invalid age!")
    
#     @name.setter
#     def name(self, name):
#         self.__name = name

#     def display_info(self):
#         print(f"Name: {self.__name}, age: {self.__age}")


# class Employee(Person):

#     def __init__(self, name, age, company):
#         Person.__init__(self, name, age)
#         self.company = company

#     def display_info(self):
#         Person.display_info(self)
#         print(f"Company name: {self.company}")

# emp = Employee("Kanat", 23, "Coca cola")
# emp.display_info()


# class Student(Person):

#     def __init__(self, name, age, university):
#         Person.__init__(self, name, age)
#         self.university = university

#     def display_info(self):
#         Person.display_info(self)
#         print(f"Student name: {self.name}, university name: {self.university}")

# st = Student("Antow", 75, "Politeh")
# st.display_info()

# class Nurbolot:

#     def __init__(self, name, age, phone):
#         self.name = name
#         self.age = age
#         self.phone = phone

#     @property
#     def name(self):
#         return self.__name 

#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @property
#     def phone(self):
#         return self.__phone

#     @phone.setter
#     def phone(self, phone):
#         if phone > 5:
#             self.__phone = phone
#         else:
#             print("Invalid number")
    
#     def display_info(self):
#         print(f"Name: {self.__name}, age: {self.__phone}")

# class A(Nurbolot):

#     def __init__(self, name, age, phone):
#         Nurbolot.__init__(self, name, age, phone)

#     def display_info(self):
#         Nurbolot.display_info(self)
#         print(f"Student name: {self.name}, university name: {self.phone}")     

# a = A("Nurba", 23, 3)
# a.display_info()






































































