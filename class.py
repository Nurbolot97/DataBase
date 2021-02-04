# # Task1
# class Student():
#     def __init__(self, name, lastname, department, year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance
    

#     def get_student_info(self):
#         print(f'{self.name} {self.lastname} postupil v {self.year_of_entrance} godu v fakultet: {self.department}')
    
    
# Vasya = Student('Vasya', 'Ivanov', 'Programming', '2017')
# Vasya.get_student_info()

# # Task2
# class BankAccount():
#     def __init__(amount, balance):
#         amount.balance = balance

#     def withdraw(amount):
#         result = amount.balance - 5
#         print(result)
    
#     def deposit(amount):
#         result = amount.balance + 10
#         print(result)

# summa = BankAccount(15)
# summa.withdraw()
# summa.deposit()

# # Task3
# class Airplane():
#     make = 'Iron'
#     model = 'Boing 737'
#     year = '2020'
#     max_speed = '1100'
#     odometer = ''
#     is_flying = ''
    
#     def __init__(self, go, rasstoyanie):
#         self.go = go
#         self.rasstoyanie = rasstoyanie

#     def take_off(self):
#         is_flying = self.go
#         print(bool(is_flying))

#     def land(self):
#         if self.go == self.go:
#             print(False)

#     def fly(self):
#         odometer = self.rasstoyanie
#         print(odometer)

# c = Airplane('Go on', '800')
# c.take_off()
# print(Airplane.is_flying)
# c.land()
# c.fly()
# print(Airplane.odometer)