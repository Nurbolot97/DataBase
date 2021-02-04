# # Task1
# class MyList(list):
#     def __init__(self, list_):
#         self.list_ = list(list_)

#     def __getitem__(self, index):
#         return self.list_[index - 1]

# x = MyList([1,8,3,4,5])
# print(x[2])

# # Task2
# class Student:
#     def init(self,name, surname, klass,  **kwargs):
#         self.name = name
#         self.surname = surname
#         self.klass = klass
#         self.kwargs = kwargs
#         self.midle = 0

#     def average_rating(self):
#         all_ = sum(self.kwargs.values())
#         self.midle = all_ / len(self.kwargs.values())
#         return self.midle

# nurba = Student('nurba', 'daiykanov', '11b', history=89, math=99, literature=86)
# asan = Student('asan', 'bakytov', '11b', history=88, math=100, literature=87)
# aidar = Student('aidar', 'alymbekov', '11b', history=87, math=101, literature=85)

