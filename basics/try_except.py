# исключения это обьекты, которые перерабатывают работу кода, если не были обработанны

'SyntaxError'
#это исключение кодгда в коде допущенф синтаксическая ошибка

'NameError'
# это исключение которое выходит, когда мы обращаемся к несуществующей переменной

'IndexError'
#исключение, которое выходит при обращении к несуществующему индексу
'''
list_ = [1,2,3,4]
list_[1000000]
'''

'KeyError'
# исключение которое выходит когда обращяемся к несуществующему ключу
'''
dict_ = []'a': 1, 'b': 2]
print(dict_['c'])
'''

'-----------------------------------'
'ValueError'
# когда мы передаем функцию некорректную для нее тип данных
'''
int('10d')
'''
#когда мы распоковываем итерируемый объект на насколько переменных и кол-во переменных не совпадает с кол-ом значений 
'''
a,b,c = [1,2]

'''


'TypeError'
# когда мы пытаемся использовать методы несвойтсвенные какому-то типу данных 
'''
for i in 123456789: (это одно число)

'''
# когда мы пытаеммся передать функцию больше или меньше аргументов, чем принимает функция
'''
5 + '5' 
'''
'''
{[1,2,3]:'a'} #ключами могут быть, только неизменяемые типы данных(лист - изменяемый тип данных)
'''

'ZeroDivisionError'
#выходит когда делим что-то на 0
'''
45/0 |100 // 0| 3 % 0
'''

'AttributeError'
#Выходит когда мы обращаемся к несуществующему аттрибуту или методу объекта (Типа данных)
'''(a = [1,2,3].replace(1,5))'''

'IndentationError'
#Когда мы неправильно используем отступы 
'''
    a = 5 


for i in range(10): ((Тоже ошибка))
print(i)
    
'''
Exception
# Исключение, которое создали, чтобы его вызывать

'+++++++++++++++++Вызов исключений+++++++++++++++++++++++++++++'
#raise ZeroDivisionError("Я вызвал ошибку")

'+++++++++++++++++Try except+++++++++++++++++++++++++++++++++++'
# Конструкция, которая помогает обрабатывать исключения.

# try: #Конструкцию try используют, если разработчик не уверен или знает, что в коде есть ошибка и хочет обработать ее в except
#     num = int(input("Введите число: "))
# except ValueError: #Конструкция except нужна для обработки исключения, в данном случае ValueError
#     print("Введите число, а не символ: ")
# else: #Работает когда не вышло ошибки, исключения(когда не работает except)
#     print(f"Вы ввели число {num}")
# finally: #Работает всегда
#     print("Пока")


try:
    raise ValueError
except Exception:
    print('Нет такой переменной, проверил вот такие исключения: NameError, TypeError,ValueError')



try:
    raise Exception
except : #Отлавливает все ошибки
    print('kish')

try:
    print(1)
except:
    print(0.1)
finally:
    print(2)

