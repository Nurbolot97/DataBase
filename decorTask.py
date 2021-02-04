# # Task1
# import datetime

# a = datetime.datetime.now()
# b = int(a.hour)

# if b in range(9, 22):
#     def decor_say_whee(my_func):
#         def wrapper():
#             my_func()
#         return wrapper
    
#     @decor_say_whee
#     def say_whee():
#         print(f"Wheeee! Time now: {a}")
#     say_whee()
# else:
#     print(f"You cannot say whee! Because time: {a}")

# # Task2
# def my_func(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('Время выполнения: {} секунд.'.format(end-start))
#     return wrapper

# @my_func
# def function():
#     print("Makers AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
# function()

# # Task3
# def decor(iters):
#     def actual_decorator(func):
#         def wrapper(name):
#             result = iters*(f'{name}\n')
#             print(result)
#         return wrapper
#     return actual_decorator

# @decor(iters=4)
# def function(name):
#     print(f"{name}")
# function("Python")

# # Task4
# users = {'Aibek': 123, 'Bek': 45, 'Adinai': 67}

# name = input("Vvedite umya: ")
# pas = int(input("Vvedite parol: "))

# def is_auth_decor(func):
#     def wrapper(func1):
#         def check(username, password):
#             if username in users.keys():
#                 if password == users.get(username):
#                     func1(username, password)
#                 else:
#                     raise Exception("Password is invalid!")
#             else:
#                 raise Exception("Username is not defined!")
#         return check
#     return wrapper
            
# @is_auth_decor(users)
# def login(username, password):
#     print(f'Welcom {username}')
# login(name, pas)

# Task5
# def my_decorator(func):
#     def inner(a, b=1, *args, **kwargs):
#         return f""" Calling testfunc {"""
        

# @my_decorator
# def testfunc(a, b=1, *args, **kwargs):
#     return a+b
# testfunc(2)





