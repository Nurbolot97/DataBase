# # Task1
# def dollarize(float):
#     return '${:,.2f}'.format(float)


# class MoneyFmt:

#     def __init__(self, amount):
#         self.amount = amount

#     def update(self, new_amount):
#         self.amount = new_amount

#     def __repr__(self):
#         return str(self.amount)

#     def __str__(self):
#         return dollarize(self.amount)

# obj = MoneyFmt(4544.4578)
# print(obj)
# obj.update(326.212)
# print(obj)
# obj.update(-0.8)
# print(obj)
# print(repr(obj))

# # Task2
# class Bike:
#     def __init__(self, cost, make, model, year, condition):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = 0 
#         self.sold = False
#         self.min_income = 1000

#     def service(self, cost_rem, novoe_sos):
#         self.cost_rem = cost_rem
#         self.novoe_sos = novoe_sos
#         result = self.sena() + self.cost_rem
#         return result

#     def sena(self):
#         return self._sale_price + self.min_income

#     def sell(self, quantity):
#         self.quantity = quantity
#         if self.quantity > 0:
#             self.sold == True
#         return self.service(100, 'new')
    
#     # @classmethod
#     # def get_default_bike(cls):
#     #     return cls([])

# bike = Bike(100, 'iron', 'ats', 2020, 'new')
# print(bike.sell(1))


# # Task3
# import random

# class Solder:
#     def init(self, gamer_id, comand, role):
#         self.gamer_id = gamer_id
#         self.comand = comand
#         self.role = role

#     @staticmethod
#     def go_after_hero(hero_id):
#         return (f'Going after hero {hero_id}')

#     @classmethod
#     def white_solder(cls):
#         return cls(1, 'white', 'solder')
    
#     @classmethod
#     def black_solder(cls):
#         return cls(2, 'black', 'solder')

# class Hero:
#     level = 1

#     def init(self, gamer_id, comand, role):
#         self.gamer_id = gamer_id
#         self.comand = comand
#         self.role = role

#     def update_level(self):
#         self.level += 1

#     @classmethod
#     def white_hero(cls):
#         return cls(1, 'white', 'hero')

#     @classmethod
#     def black_hero(cls):
#         return cls(2, 'black', 'hero')

# whits = []
# blacks = []
# for i in range(11):
#     a = random.randrange(1, 3)
#     if a == 1:
#         solder = Solder(i, 'white', 'solder')
#         whits.append(solder.gamer_id)
#     elif a == 2:
#         solder = Solder(i, 'black', 'solder')
#         blacks.append(solder.gamer_id)

# if len(whits) > len(blacks):
#     hero = Hero.white_hero()
#     hero.update_level()
#     solder = Solder.white_solder()
#     print(solder.go_after_hero(hero.gamer_id))
#     print(solder.gamer_id)

# elif len(whits) < len(blacks):
#     hero = Hero.black_hero()
#     hero.update_level()
#     solder = Solder.black_solder()
#     print(solder.go_after_hero(hero.gamer_id))
#     print(solder.gamer_id)





















































