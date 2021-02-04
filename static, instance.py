# class MyClass:
#     def method(self):                           #can modify object instance
#         return 'instance method called', self   #can modify class

#     @classmethod
#     def classmethod(cls):                       #cannot modify object instance
#         return 'class method called', cls       #can modify class
    
#     @staticmethod
#     def staticmethod():                         #cannot modify object instance
#         return 'static method called'           #cannot modify class

# obj = MyClass()

# print(obj.method())
# print(obj.classmethod())
# print(obj.staticmethod())

# from math import pi
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     def __str__(self):
#         return f"Pizza ({self.ingredients})"
    
#     @classmethod
#     def four_cheese(cls):
#         return cls(['blue', 'holland', 'mozarello', 'dorblue'])
    
#     @classmethod
#     def chuchuk_pizza(cls):
#         return cls(['chuchuk', 'may', 'caryn'])

#     @staticmethod
#     def circle_area(r):
#         return r**2*pi
    
# margarita = Pizza(['tomato', 'cheese'])
# print(margarita)
# print(margarita.circle_area(10))

# four = Pizza.four_cheese()
# print(four)

# three = Pizza.chuchuk_pizza()
# print(three)

















