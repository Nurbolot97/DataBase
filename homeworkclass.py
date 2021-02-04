# # Task1
# class ContactList(list):
#     def __init__(self, *args):
#         self.args = args


#     def get_name(self, name):
#         self.name = name
#         list1 = []
#         for i in list_:
#             if i.lower().startswith(self.name.lower()):
#                 list1.append(i)
#         return list1



# list_ = ['Asan', 'Aibek', 'Bek']
# all_contacts = ContactList(list_)     

# print(all_contacts.get_name('A'))

# # Task2
# class User:
#     def __init__(self, firstname, lastname, age, email):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.email = email

#     def describe_user(self):
#         print(f"{self.firstname} {self.lastname} rodilsya 1989 godu, seichas emu: {self.age}. Ego email: {self.email}")
    
#     def greet_user(self):
#         print(f"Welcom {self.firstname} {self.lastname}!")

# class Admin(User):
#     def __init__(self, firstname, lastname, age, email, priveleges):
#         User.__init__(self, firstname, lastname, age, email)
#         self.priveleges = priveleges
#     def show_priveleges(self):
#         print(f"{self.priveleges}")

# ekzem = Admin('Asan', 'Amanov', 35, 'asan@mail.ru', 'mojno dobavlyat')
# ekzem.describe_user()
# ekzem.greet_user()
# ekzem.show_priveleges()

# # Task3
# class House:
#     house_type = 'mansard'
#     plowad = 15
#     list_mebel = ['krovat', 'wkaf', 'stol']
#     krovat = 4
#     wkaf = 2
#     stol = 1.5

#     def inform(self):
#         print(self.house_type, self.list_mebel, self.plowad, self.plowad - self.krovat - self.wkaf - self.stol)

# a = House()
# a.inform()

# Task4


