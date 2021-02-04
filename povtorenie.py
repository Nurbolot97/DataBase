# class User:
#     def __init__(self, email_param):
#         self.email = email_param

#     @property
#     def email(self):
#         return f"{self._email}"

#     @email.setter
#     def email(self, email_param):
#         if "@" in email_param:
#             self._email = email_param
#         else:
#             print("Invalid email")
# user = User("12345678@90")
# print(user.email)

# import random


# class Human:
#     id_ = 0
#     def __init__(self, team):
#         self.id_ = Human.id_ + 1
#         self.team = team
    
#     @property
#     def uniq_id(self):
#         self.id = id

        

# class Hero(Human):

#     def __init__(self, team):
#         super().__init__(team)
#         self.level = 0
    
#     def level_up(self, num):
#         self.level += num


# class Soldier(Human):
    
#     def follow_hero(self, hero):
#         self.follow = hero

# team1 = []
# team2 = []
# team3 = []
# team4 = []
# teams = [team1, team2, team3, team4]
# soldiers = []

# d = {}

# for num in range(20):
#     soldiers_team = random.choice(teams)
#     d["soldier{0}".format(num)] = Soldier(soldiers_team)
#     soldiers_team.append(d["soldier{0}".format(num)])
#     soldiers.append(d["soldier{0}".format(num)])

# for sol in soldiers:
#     print(one.id)

# for count, team in enumerate(teams, start=1):
#     print(f"{team} contains {len(team)} soldiers")

























