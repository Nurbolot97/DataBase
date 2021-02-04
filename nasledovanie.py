# #OOP
# class Human:
#     hands = 2
#     legs = 2


#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

# class Student(Human):
#     pass


# ermek = Human('Ermek', 'Boronov')
# ulan = Student('Ulan', 'Ormonov')
# print(ulan.legs)

# print(ermek.__dict__)
# print(ulan.__dict__)
# print(isinstance(ermek, Human))
# print(issubclass(Student, Human))

# class Grandparent:

#     #Constructor
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name

# class Parent(Grandparent):

#     #Constructor
#     def __init__(self, name, age):
#         Grandparent.__init__(self, name)
#         self.age = age

#     def get_age(self):
#         return self.age


# class Child(Parent):

#     #Constructor
#     def __init__(self, name, age, phone):
#         Parent.__init__(self, name, age)
#         self.phone = phone

#     def get_phone(self):
#         return self.phone


# Ivan = Child('Ivan', 23, '123456789')
# print(Ivan.get_name(), Ivan.get_age(), Ivan.get_phone())

# print(Child.mro())










