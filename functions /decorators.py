'++++++++++++++++Функция высшего порядка++++++++++++++++++'
#Функция высшего порядка - это функция которая принимает аргументы в другую функцию, создает внутри себя другую функцию,
#вызывает функцию и возвращает функцию

# def func1():
#     return 'hi'
# def func2(func_):
#     print(func_())

# func2(func1) #func2 высший порядок так как в нее передают другую функцию

'+++++++++++++++Декораторы++++===++++++++++++++++++='
#Декораторы - Функция высшего порядка, которая нужна для расширения функционала другой функции не изменяя ее. (функция оберток)

# def decorator_glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text
#         print(res)
#     return wrapper
# # @decorator_glushitel
# def gun():
#     return 'стрелять'
# # gun()
# wrapper = decorator_glushitel(gun)
# wrapper()#способ использовать декоратор вручную 
'------------------------------------------------'
# def decorator_glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text
#         print(res)
#     return wrapper
# @decorator_glushitel
# def gun():
#     return 'стрелять'
# gun()#спосоп использовать декоратор при помощи синтаксического сахара
'--------------------------------------------------------------------'
from datetime import datetime
# def decorator(func):
#     def wrapper():
#         print('start: ',datetime.now())
#         func()
#         print('finish: ',datetime.now())
#     return wrapper
# # @decorator
# def hello():
#     print('hello world')
# wrapper = decorator(hello)
# wrapper()
'--------------------------------------------------------------------'
# def func_start_time(func):
#     def wrapper(*args, **kwargs):
#         print('start: ', datetime.now())
#         func(*args, **kwargs)
#         print('end: ', datetime.now())
#     return wrapper

# @func_start_time
# def sum_(a,b):
#     print(a + b)

# sum_(20,10)
'---------------------------------------------------------------------'
# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator

# @decorator(10)
# def hello(): 
#     print('hello world')

# hello()
