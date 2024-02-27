'++++++++++++++++++++++++Функция++++++++++++++++++++++++++++'
# Функция это именованный блок кода, который может принимать аргумент и возвращать результат 

# def get_sum(x,y): # x, y - это параметры
#     result = x + y
#     return result

# print(get_sum(1,2)) #1, 2 -  это аргументы
 

# def pow_ (a,b):
#     result = a**b
#     return result
# print(pow_(2,2))

"Функции соблюдают принцип DRY"
"Don't repeat yourself"

'+++++++++++++++++++Аргументы и параметры+++++++++++++++++++++'
#Параметры - это переменные внутри функции, задаются при создании функции 
#Аргументы  - это значения, которые мы передаем при вызове функции 

"+++++++++++++++++++Виды параметров++++++++++++++++++++"
#1. Обязательны
#2. нобязательные
#   1. с дефолтным значением(со значением по умолчанию)
#   2. *args(все позиционный аргумент) ((tuple))
#   3. **kwargs(все лишние именнованные аргументы) ((dict)) *key *value

# def func_(a,b):
#     return a+b
# # print(func_(10,5))

# def my_func(*args):
#     print(args)
# my_func(12,3,23,23,45,234,5, 'asdfqwg')

# def my_func(*args,**kwargs):
#     print(*args)
#     print(kwargs)
# my_func(12,3,23,23,45,234,5, hello = 'hello')


'+++++++++++++Виды аргументов++++++++++++++++'
# 1.Позиционные (по позиции)
# 2.Именнованные (по названию (памаметр = значение))


# def fucn(a,b,c):
#     pass
# fucn(b=2,c=2,a=1)
# #именнованный 


'----------------------------------------'
# num: int=10
# name: str = 'makers'

# def sum_ (a:int, b:int):
#     return a+b
# print(sum_(100,2))


# def calc():

#     try: 
#         num1 = float(input('Enter number: '))
#         num2 = float(input('Enter number: '))
#         oper = (input('Enter operator: '))
#         if oper == "+":
#             print(num1+num2)
#         elif oper == "-":
#             print(num1-num2)
#         elif oper == '/':
#             print(num1/num2)
#         elif oper == '*':
#             print(num1*num2)
#         elif oper == '**':
#             print(num1**num2)
#         else: 
#             raise KeyError
#     except KeyError:
#         print("Вы ввели не тот символ")
#     except ValueError:
#         print("Введите число, а не символ")
#     except ZeroDivisionError:
#         print('Нельзя делить на 0')

# calc()
'-----------------------------------------------------------------'
# db = [
#     {"name":"Termirlan", "password":hash('123456789')},
#     {"name":"Kutman", "password":hash('0987654321')}
#     ]
# def in_database(name):
#     for user in db:
#         if name == user['name']:
#             return True
#     return False

# def register(name,password, password2):
#     if in_database(name): 
#         raise Exception('Такое имя уже существует')
#     if password != password2:
#         raise Exception('Пароли не совпадают')
#     user = {'name':name, 'password':hash(password)}
#     db.append(user)
#     return 'Вы успешно зарегистрировались'

# def login(name, password): 
#     if not in_database(name):
#         raise Exception('Пользователь не найден')
#     for user in db: 
#         if user['name'] == name :
#             if user['password'] != hash(password):
#                 raise Exception('Пароль неверный!')
            
#     return 'Добро пожаловать'
# print(register('nick','123','123'))
# print(login('nick','12hhh3'))
# print(db)
'------------------------Lambda------------------------------------'
# lambda - это анонимная функция, которая записывается в одну строчку, одноразовая

# def sum1(y):
#     return y**2
# sum1(2)
# sum1(4)

# sum_ = lambda y: y**2
# sum_(2)