# # Task1
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.fuel = 70

#     def drive(self, distance):
#         self.distance = distance
#         if self.fuel*10 > self.distance:
#             print("Let's drive")
#         else:
#             print("Need more fuel, please, fill more!")
    
#     def __add_distance(self):
#         self.odometer = 0
#         self.odometer += self.distance
#     def __subtract_fuel(self):
#         self.fuel = 70
#         self.fuel -= self.distance/10


# car1 = Car('iron', 'opel', 2005)
# car1.drive(800)
# car1._Car__add_distance()
# car1._Car__subtract_fuel()
# print(car1.odometer)
# print(car1.fuel)

# # Task2
# class Mobile:
#     _imei = 34343
#     _power = 100
#     _OS = 'Ios'
#     if _power == 0:
#         print("Low battery")
#     else:
#         def dostup(self):
#             self._power -= 0.5*100/100

#         def music(self):
#             self._power -= 5*100/100
        
#         def video(self):
#             self._power -= 7*100/100
#             if self._power < 10:
#                 print("You cannot watch video")

# m1 = Mobile()
# m1.dostup()
# m1.music()
# m1.video()
# print(m1._power)


# Task3
class Piramida:
    _dlina = 4
    _all_dlina = _dlina*4
    _rebro = 
