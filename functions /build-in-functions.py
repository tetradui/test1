'=======Встроенные функции=========='
# map , filter, reduce, zip, enumerate.

'ZIP'
# соединяет несколько последовательностей (получаем генератор , в котором элемнты -tuple)(zip object)

# list_1 = [1,2,3,4]
# list_2 = ['a','b','c']
# list_3 = [10.5, 20.0, 1.3, 0.5]

# zipped = zip(list_1,list_2,list_3)
# print(zipped) # <zip object at 0x7f8ajs23fs>
# print(list(zipped))#[(1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3)]
# print(tuple(zipped)) # будет работать если убрать print list

'ENUMERATE'
#Нумерует последовательность (по дефолту с 0), (тоже возвращает генератор)
#<enumerate object 0x7kjf8392sjd90>

# enumerated = enumerate([True, 'hi', 1, None])
# print(enumerate) #<enumerate object 0x7kjf8392sjd90>
# # print(list(enumerated))#[(0, 'h'),(1, 'e'),(2, 'l'),(3, 'l'),(4, 'o'),(5, ' '),(6, 'w'),(7, 'o'),(8, 'r'),(9, 'l'),(10, 'd')]
# for elem in enumerated: 
#     print(elem)

'MAP'
# Функция высшего порядка - это функция^, которая принимает аргументы в другую функцию, создает внутри себя другую функцию,
#вызывает функцию и возвращает функцию 
#MAP принимаем 1)функцию и 2)последовательность 
#Он записывает в новую последовательность результат функции, применив ее на каждый элемент последовательности 
#<map object ...>

# list_ = ['1','2','3','4']
# mapped = map(int, list_)#<map object ...>
# print(list(mapped))

# mapped2 = map(str.isdigit, list_)
# print(list(mapped2))

# list_ = [12,3,4,40,23,4]
# def pow_(x):
#     return x**2
# print(list(map(pow_,list_)))
# print(list(map(lambda x:x**2, list_)))
str_ = 'hello world'
mapped = map(str.upper, str_)
print(''.join(mapped))

# print(''.join(list(map(str.upper, 'hello world'))))

'FILTER'
#Возвращает генератор с элементами, прошедшими фильтрацию (какое-то условие), принимает функцию и последовательность
#<filter object 0x7jdfj9292k29>
# list_ = [1,2,-34,5,-233,54,0]
# def fil(x): 
#     return x>=0
# filtered = filter(fil, list_)
# print(list(filtered))

# users = [
#     {'name':'makers', 'age':20},
#     {'name':'anonim', 'age':15},
#     {'name':'lexa',   'age':23},
#     {'name':'Anonim', 'age':15}
# ]
# filtered = filter(lambda x: x['name'].startswith('a') or x['name'].startswith('A'), users )
# print(list(filtered))

'REDUCE'
# принимает функцию и последовательность, но возвращает 1 элемент (передаемая функция должна принимать 2 аргумента)
# импортируется из functools
from functools import reduce
# list_ = [1,22,3,4]
# res = reduce(lambda x,y:x*y,list_ )
# print(res)



# users = [
#     {'name':'makers', 'age':20},
#     {'name':'anonim', 'age':15},
#     {'name':'lexa',   'age':23},
#     {'name':'Anonim', 'age':1}
# ]
# def func (x,y): 
#     if x['age'] > y['age']:
#         return x
#     else:
#         return y
    
# reduc = reduce(func, users)
# print((reduc))

# list_ = [1,2,4,6,1,9,-1,6,-12]
# def min_(x,y):
#     if x<y:
#         return x
#     else: 
#         return y
# red = reduce(min_, list_)
# red1 = reduce(lambda x,y: x if x<y else y, list_)
# print(red)
# print(red1)

