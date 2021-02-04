# # Task1
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.odometer = 0
#         self.year = year
#         self.fuel = 70

#     def drive(self, distance):
#         self.distance = distance
#         if self.distance < self.fuel*10:
#             print("Lets drive!")
#             self.__add_distance()
#             self.__subtract_fuel()
#         else:
#             print("Need more fuel, please, fill more!")

#     def __add_distance(self):
#         self.odometer += self.distance

#     def __subtract_fuel(self):
#         self.fuel -= self.distance/10

# a = Car('iron', 'opel', 1997 )
# a.drive(600)


# # Task2
# class Coder:
#     def __init__(self, experience, count_code_time):
#         self.experience = experience
#         self.count_code_time = 0

#     def get_info(self):
#         return NotImplementedError
#     def coding(self):
#         return NotImplementedError


# class Backend(Coder):
#     def __init__(self, experience, count_code_time, languages_back):
#         Coder.__init__(self, experience, count_code_time)
#         self.languages_back = languages_back

#     def get_info(self):
#         return NotImplementedError

#     def coding(self, coding_time):
#         self.coding_time = coding_time
#         self.count_code_time += self.coding_time


# class Frontend(Coder):
#     def __init__(self, experience, count_code_time, languages_front):
#         Coder.__init__(self, experience, count_code_time)
#         self.languages_front = languages_front

#     def get_info(self):
#         return NotImplementedError

#     def coding(self, coding_our):
#         self.coding_our = coding_our
#         self.count_code_time += self.coding_our

# a = Frontend(45, 0, "js")
# a.coding(100)
# print(a.count_code_time)
# b = Backend(10, 0, "python")
# b.coding(200)
# print(b.count_code_time)


# class Fullstack(Backend, Frontend):
#     def __init__(self, experience, count_code_time, languages_back, languages_front):
#         Coder.__init__(self, experience, count_code_time)
#         self.languages_back = languages_back
#         self.languages_front = languages_front
    
#     def get_info(self):
#         return NotImplementedError

#     def coding(self, coding_chasy):
#         self.coding_chasy = coding_chasy
#         self.count_code_time += self.coding_chasy

# c = Fullstack(20, 0, "pyhton", "js")
# c.coding(500)
# print(c.count_code_time)

# # Task3
# class Person:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#     def get_info(self):
#         return f"Hello my name is  {self.name} {self.lastname}"

# class Employee:
#     def __init__(self, name, lastname, company, doljnost):
#         Person.__init__(self, name, lastname)
#         self.company = company
#         self.doljnost = doljnost
#     def get_info(self):
#         return f"Hello my name is  {self.name} {self.lastname}. I work at {self.company} in position {self.doljnost}"

# class Student:
#     def __init__(self, name, lastname, university, course):
#         Person.__init__(self, name, lastname)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f"Hello my name is  {self.name} {self.lastname}. I study at {self.university} in level {self.course}"

# s1 = Employee("Ivan", "Petrov", "Facebook", "program")
# print(s1.get_info())
# s2 = Student("Ivan", "Petrov", "KGTU", 3)
# print(s2.get_info())

# # Task4
# class Student:
#     def __init__(self, name, lastname, level, marks):
#         self.name = name
#         self.lastname = lastname
#         self.level = level
#         self.marks = marks #dictionary

#     @property
#     def average(self):
#         return sum(self.marks.values())/len(list(self.marks.values()))

#     def __eq__(self, other):
#         return self.average == other.average

#     def __gt__(self, other):
#         return self.average > other.average

# st1 = Student('Asan', 'Asanov', 11, {'history': 89, 'math': 100, 'literature': 88})
# st2 = Student('Aigul', 'Esenov', 10, {'history': 70, 'math': 65, 'literature': 55})
# print(st1 == st2)
# print(st1 > st2)


    



