# # # Task1
# # import datetime

# # class Clock:
# #     def time(self):
# #         self.time = datetime.datetime.now().time()
# #         print(self.time)

# # class AlarmMixin:
# #     def turn_on(self):
# #         self.vrem1 = "Get up"

# #     def turn_off(self):
# #         self.vrem2 = "Mojno ne vstavat"

# # class AlarmClock(Clock, AlarmMixin):
# #     def budilnik(self):
# #         if self.time == datetime.time(21,00,00):
# #             print(self.vrem1)
# #         else:
# #             print(self.vrem2)

# # a = AlarmClock()
# # a.time()
# # a.turn_on()
# # a.turn_off()
# # a.budilnik()


# # Task2
# # class Coder:
# #     def __init__(self, experience, count_code_time):
# #         self.experience = experience
# #         self.count_code_time = count_code_time

# #     def get_info(self):
# #         print(f"Experience: {self.experience}, coding: {self.count_code_time}")

# #     def coding(self):
# #         return NotImplemented


# # class Backend(Coder):
# #     def __init__(self, experience, count_code_time, languages_backend):
# #         super().__init__(experience, count_code_time)
# #         self.languages_backend = languages_backend
    
# #     def coding(self, chasy):
# #         self.count_code_time += chasy
    
# #     def get_info(self):
# #         print(f"Experience: {self.experience}, coding: {self.count_code_time}, languages_backend: {self.languages_backend}")

# # class Frontend(Coder):
# #     def __init__(self, experience, count_code_time, languages_frontend):
# #         super().__init__(experience, count_code_time)
# #         self.languages_frontend = languages_frontend

# #     def coding(self, chasy):
# #         self.count_code_time += chasy

# #     def get_info(self):
# #         print(f"Experience: {self.experience}, coding: {self.count_code_time}, languages_backend: {self.languages_frontend}")
    
# # student1 = Backend(10, 30, 'python')
# # student1.coding(50)
# # student1.get_info()

# # student2 = Frontend(15, 40, 'java script')
# # student2.coding(30)
# # student2.get_info()

   
# # # Task3
# # import random
# # from random import shuffle

# # class Coloda:
# #     def __init__(self, chervy, trefy, bubny, piki,all_cards):
# #         self.chervy = chervy
# #         self.trefy = trefy
# #         self.bubny = bubny
# #         self.piki = piki
# #         self.all_cards = all_cards

# # class Card(Coloda):
# #     def mix(self):
# #         random.shuffle(self.all_cards)
# #         print(len(all_cards))

# #     def deal(self):
# #         print(all_cards.pop())
        
# # piki = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# # chervy = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# # trefy = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# # bubny = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# # all_cards = piki + chervy + trefy + bubny
# # w1 = Card(chervy, trefy, bubny, piki, all_cards)
# # w1.mix()
# # w1.deal()

# # Task4


# Alisher:
# from datetime import datetime

# class Clock:
#     def show_current_time(self):
#         print(datetime.now())



# class Alarm:

#     switcher = 1

#     def turn_alarm_on(self):
#         Alarm.switcher = 1

#     def turn_alarm_off(self):
#         Alarm.switcher = 0


# class AlarmClock(Alarm, Clock):
#     def set_alarm(self, time):
#         self.time = time
#         while Alarm.switcher == 1:
#             hour = datetime.now().hour
#             minute = datetime.now().minute
#             curr_time = f"{hour}:{minute}"
#             if self.time == curr_time:
#                 print("It's time to wake up!")
#                 break
#             else:
#                 print('Not now')
#                 break


# get_up = AlarmClock()
# get_up.set_alarm("21:10")
# get_up.turn_alarm_off()

# Ло:
# class Coder:
#     count_code_time = 0
#     def init(self, experience):
#         self.experience = experience

#     def get_info(self):
#         return f'experience: {self.experience}, count_code_time: {self.count_code_time}'

#     def coding(self, coding_time):
#         try:
#             self.count_code_time += coding_time
#         except NotImplementedError:
#             raise Exception('NotImplementedError')


# class Backend(Coder):
#     def init(self, languages_backend, coding_time):
#         self.languages_backend = languages_backend
#         super().__init__(languages_backend)
#         super().coding(coding_time)

#     def get_info(self):
#         return super().get_info()


# class Frontend(Coder):
#     def init(self, languages_frontend, coding_time):
#         self.languages_frontend = languages_frontend
#         super().__init__(languages_frontend)
#         super().coding(coding_time)

#     def get_info(self):
#         return super().get_info()


# class Fullstack(Backend):
#     def init(self, languages, coding_time):
#         self.languages = languages
#         super().__init__(languages, coding_time)

#     def get_info(self):
#         return super().get_info()


        
# python = Backend('Python', 5)
# print(python.get_info())

# js = Frontend('JS', 3)
# print(js.get_info())

# php = Fullstack('php', 4)
# print(php.get_info())

# hallo:
# class Coder:
#     experience = 3
#     count_code_time = 0 
#     def get_info(self):
#         raise NotImplementedError

#     def coding(self):
#         raise NotImplementedError

# class Backend(Coder):
#     languages_backend = 'Python'

#     def get_info(self):
#         return self.count_code_time, (self.experience,'года работы')
    
#     def coding(self, quantity):
#         self.count_code_time += quantity
        

# class Frontend(Coder):
#     languages_fronted = 'JS'
 
#     def get_info(self):
#         return self.count_code_time, (self.experience,'года работы')
    
#     def coding(self, quantity):
#         self.count_code_time += quantity

# class FullStack(Backend, Frontend):
#     pass
    

# python = Backend()
# print(python.coding(5), python.get_info())
# print(python.coding(5), python.get_info())
# print(python.languages_backend)

# javascript = Frontend()
# print(javascript.coding(5), javascript.get_info())
# print(javascript.coding(5), javascript.get_info())
# print(javascript.languages_fronted)


# full = FullStack()
# print(full.coding(5), full.get_info())
# print(full.coding(5), full.get_info())
# print(full.languages_backend, full.languages_fronted)

# Batyrzhan uulu:
# class Coder:
#     def init(self, experience):
#         print("INIT OF CODER")
#         self.experience = experience
#         self.count_code_time = 0

#     def get_info(self):
#         raise NotImplementedError
#         # return f'experience: {self.experience}, count_code_time: {self.count_code_time}'

#     def coding(self, coding_time):
#         raise NotImplementedError


# class Backend(Coder):
#     def init(self, experience, *args):
#         Coder.__init__(self, experience)
#         self.languages = args
        

#     def coding(self, coding_time):
#         self.count_code_time += coding_time

#     def get_info(self):
#         return f'experience: {self.languages}, count_code_time: {self.count_code_time}'


# class Frontend(Coder):
#     def init(self, experience, *args):
#         print('INIT  OF FRONTEDNT')
#         su
# per().__init__(experience)
#         self.languages_frontend = args
        

#     def coding(self, coding_time):
#         self.count_code_time += coding_time

#     def get_info(self):
#         return f'experience: {self.experience}, count_code_time: {self.count_code_time}'


# class Fullstack(Backend, Frontend):
#     pass

# python = Backend(5, 'Python')
# print(python.get_info())

# js = Frontend(3, 'JS')
# print(js.get_info())
# print(Fullstack.mro())
# php = Fullstack(10, 'Python', 'Dart')
# print(php.get_info())

# 𝓬𝔀𝓪𝓻𝓴𝓴:
# class Card:
#     suits = ["clubs", "diamonds", "hearts", "spades"]
#     ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


# class Deck:
#     def deal(self):
#         random.shuffle(Card.suits)
#         random.shuffle(Card.ranks)
#         print(Card.suits[-1], Card.ranks[-1])

#     def mix(self):
#         cards = 52
#         sum_of_cards = len(Card.suits) * len(Card.ranks)
#         if sum_of_cards == cards:
#             print("The deck counts 52 card")
#         else:
#             raise Exception("Someone is fooling us")
#         mixed_deck = []
#         for suit in Card.suits:
#             for rank in Card.ranks:
#                 mixed_deck.append((suit, rank))
#         random.shuffle(mixed_deck)
#         mixed_deck.pop()
#         print(mixed_deck)


# play = Deck()
# play.deal()
# play.mix()

# Batyrzhan uulu:
# import random

# class Card:
#     suits = ["clubs", "diamonds", "hearts", "spades"]
#     ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


# class Deck:
#     def deal(self):
#         mixed_deck = []
#         for suit in Card.suits:
#             for rank in Card.ranks:
#                 mixed_deck.append((suit, rank))
#         dealed_card = mixed_deck.pop()
#         print(dealed_card)


#     def mix(self):
#         cards = 52
#         sum_of_cards = len(Card.suits) * len(Card.ranks)
#         mixed_deck = []
#         if sum_of_cards == cards:
#             print("The deck counts 52 card")
#             for suit in Card.suits:
#                 for rank in Card.ranks:
#                     mixed_deck.append((suit, rank))
#             random.shuffle(mixed_deck)
#             print(mixed_deck)
#         else:
#             raise Exception("Someone is fooling us")
        
        


# play = Deck()
# play.deal()
# # play.mix()



















