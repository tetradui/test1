'+++++++++++++++++++++++Области видимости++++++++++++++++++'
#LEGB - local enclosed global build-in

'+++++++++++++++++++++++Build-in+++++++++++++++++++++++++++'
#  Встроенное пространство имен таких как (list, print, dict, len, input)

'+++++++++++++++++++++++Global +++++++++++++++++++++++++++'
#Все переменные, которые мы создали внутри файла
#Чтобы посмотреть все глобальные переменные, можно использовать функцию globals
a = 10 
b = 'hello'
print(globals())
'+++++++++++++++++++++++enclosed+++++++++++++++++++++++++++'
#замкнутое пространство имен - это локальное простанстранство, у которого есть внутреннее локальное пространство

# var = 'global'# хранится в глобальном пространстве 

# def func():
#     var = 'enclosed' #замкнутое пространство 
#     def inner_func():
#         var = 'local'#Локальное пространство 
#         print(var)
#     print(var)
#     inner_func()
# print(var)
# func()


'=++++++++++++++++++local+++++++++++++++++++++++'
#Локальное пространство имен - это пространство, которое находится внутри в функции

a = 10 
def func(a,b):
    res = a+b
    print(res)
    print(locals())
func(10,5)


# count = 0
# def count_():
#     global count
#     count += 1
#     print(count)
# count_()
# count_()
# count_()

# def count_(num):
#     count = 0
#     def inner_count():
#         nonlocal count
#         count += 1
#         print(count)
#     for i in range(num):
#         inner_count()
# count_(10)


