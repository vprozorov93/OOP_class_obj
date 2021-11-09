# # print(dir(str))
#
# class Person:
#     # name = '' # все заначения класса можно инициализировать в методе init, тогда данные значения будут инициализироваться
#     # power = 0 # в момент создания объекта класса, а не при его объявлении в программе
#     # energy = 100
#     # hands = 2
#     # backpack = [] # значение инициализируется присоздании класса, а изменяемые типы ссылаются на один и тот же объект
#     #               в памяти, то есть они будут общими у экземпляра класса. Поэтому не нужно делать изменяемые типы
#     #               значением по умолчанию для аругментов. Аргумент backpack как раз укладывается в это описание.
#
#     # Аргумент методов (функций класса) self ссылается на кокретный экземпляр класса (который еще не создан)
#     # Его обязательно нужно указывать, что бы показывать то,
#     # что все действия выполняемые методом выполняются именно с тем объектом, для которого вызывается метод
#     def __init__(self, name, power, energy=100, hands=2): # инициализатор объекта класса
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.backpack = [] # в данном случае создается атрибут рюкзак уже для конкретного объекта класса
#     #                           и не будет являться атрибутом самого класса по умолчанию
#         self.hands = hands
#
#     def eat(self, food):
#         if self.energy <100:
#             self.energy += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#
#     def change_alias(self, new_alias):
#         # print(self.alias)
#         self.alias = new_alias
#         print(self.alias)
#
#     # в методы класса можно передавать объекты класса и с ними работать
#     def beat_up(self, foe):
#         if not isinstance(foe, Person): # проверка на то, что foe является объектом класса Person
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat!')
#
# # peter = Person() # такая инициализация испольщуется, когда нет метода __init__ у класса
# # peter.name = "Peter Parker"
# # peter.power = 70
# # peter.alias = 'Spider-Man' # можно добавлять атрибуты, которые не описаны в классе, для конкретного объекта этого класса
# # # print(peter.__dict__) # покажет атрибуты объекта, которые отличаются от атрибутов класса
# # # print(Person.__dict__) # покажет все атрибуты присущие классу
# # # print(type(peter))
#
# # bruce = Person()
# # bruce.name = "Bruce Wayne"
# # bruce.power =85
# # # bruce.alias = 'Batman'
# #
# # bruce.change_alias('Robin')
#
# peter = Person('Peter Parker', 70) # такая инициализация используется, в случае если у класса присутствует метод  __init__
# bruce = Person('Bruce Wayne', 85)
#
