'++++++++++++++++++++++Словари+++++++++++++++++++'
# dict - изменяемый, итерируемый, неупорядочный, неиндексируемый тип данных, для хранения данных в парах(ключ:значение)

# user = {'name': 'Kutman', 'age': 20, 'nickname':'клинер'}
# print(user['age'])#20
# print(user['name'])#Kutman
# print(user['nickname'])#клинер


# {ключ:значение, ключ:значение...}
# Ключем могут быть только неизменяемый тип данных, уникальный(если ключ повторяется, то сохранится тот, который яв-ся последним)
# Значение любые типы данных(изменяемый и неизменяемые) Могут повторяться.

'+++++++++++++++++++++++++Создание++++++++++++++++++++++++++++++++'
# dict1 = {'a':1, 'b':2}
# dict2 = dict([('a',1),('b',2)])
# dict3 = dict(['a1', 'b2'])
# dict4 = {}
# dict4['name'] = 'tima'
# dict4['age'] = 45
# dict4['nickname'] = 'Temirlan'
# print(dict4)

'+++++++++++++++++++++++++Методы словарей++++++++++++++++++++++++++'
# get - метод, который возвращает значение по ключу, если такого ключа нет, то возвращает дефолтное значение, чаще всего None

user ={
    'name':'John',
    'age': 100,
    'telephon_number':'+1234567'
}
# print(user['asdfqf']) KeyError
# print(user.get('name')) #John
# print(user.get('ываыв', 'нет такого ключа')) #None
# print(user.get('age', 'нет такого ключа')) #100
# print(user.get('id')) #None


# #pop - удаляет пару по ключу и возвращает значение
# dict_ = {
#     'a':1,
#     'b':2,
#     'c':3
# }
# popped_values = dict_.pop('a')
# print(popped_values) #1
# print(dict_) #'b':2, 'c':3


#popitem - удаляет последнюю пару и возвращает ее.

# dict1 = {'a':1, 'b':2, 'c':3}
# popped_values = dict1.popitem()
# print(popped_values)#('c', 3) tuple


# update - расширяет словарь парами из второго словаря

dict1 = {1:'a', 2:'b'}
# dict2 = {3:'c', 4:'d'}
# dict1.update(dict2)
# print(dict1)

# # clear - очищает словарь
# dict_only = {1:'saf', 2:'wqef'}
# dict_only.clear()
# print(dict_only)

# # fromkeys - метод  для создания нового словоря, используя список ключей

# somedict = dict.fromkeys([1,2],'clown')
# print(somedict)

# dict2 = dict.fromkeys('aewfq',0)
# print(dict2)#'a':o, 'e':0, и тд

# items - метод, который достает [(ключ, значение), (ключ,значение)...]tuple 
# kyes - метод, который возравщает ключ 
# values - метод, который возвращает значения 

# dict0 = {'a':1, 'b':2, 'c':3}
# print(dict0.values())
# print(dict0.keys())
# print(dict0.items())

#zip() создает словарь из двух списков
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = (dict(zip(list1, list2)))
# print(dict_)


'+++++++++++++++++++++++Циклы с dict++++++++++++++++++++++'

dict1 = {'a':1, 'b':2, 'c':3}


for i in dict1.items():
    print(i)

