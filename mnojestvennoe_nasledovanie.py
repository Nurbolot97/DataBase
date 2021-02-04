# class Parent:
#     def __init__(self):
#         self.parent_attribute = 'I am a parent'

#     def parent_metod(self):
#         print('Back in my day.....')

# # Создаем дочернй класс, который наследуется от родительского
# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         self.child_attribute = 'I am a child'

# # создаем экземпляр
# child = Child()

# # Печатаем атрибуты и методы дочернего класса
# print(child.child_attribute)
# print(child.parent_attribute)
# child.parent_metod()

# class B:
#     def b(self):
#         print('B')

# class C(B):
#     def c(self):
#         print('C')

# class D(C,B):
#     def d(self):
#         print('D')

# d = D()
# d.b()
# d.c()
# d.d()
# print(D.mro())





# class O: pass
# class A(O): pass
# class B(O): pass
# class C(O): pass
# class D(O): pass
# class E(O): pass

# class K1(A, B, C): pass
# class K2(A, B, D): pass
# class K3(C, D ,E): pass


# class Z(K1, K2, K3): pass


# def print_mro(T):
#     print(*[c.__name__ for c in T.mro()], sep=' ---> ')

# print_mro(Z)

# class Test:
#     pass

# test = Test()


# class CraneMixin:
#     def lift(self, thing):
#         print(f"{thing} is lifted")


# class Transport:
#     def go(self):
#         print("Whoom")


# class Car(Transport):
#     def transport_passengers(self):
#         print('Transport passengers')

# class TruckWithCrane(Transport, CraneMixin):
#     def carry_things(self):
#         print('Carruing things')

# class BoatWithCrane(Transport, CraneMixin):
#     def dock(self):
#         print('Stopped and docked')


# boat = BoatWithCrane()
# boat.lift('Container')
# boat.go()
# boat.dock()









