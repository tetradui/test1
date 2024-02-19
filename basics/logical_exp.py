# '++++++++++++++++++Логические и условные операторы++++++++++++++++++++'
# #Логические операторы  - это выражения, которые возвращают True, а если неверно, то False.

# 'Сравнения'
# #Равно ==
# 5 == 6 #False 
# 5 == 5 #True 
# #Не равно !=
# 4 != 5 #True
# 5 != 5 #False 
# #Меньше 
# 10 > 0#True
# -5 > 2#False

# #меньше 
# 0 < 1 #True
# 2 < 1 #False

# #Больше или равно
# 3 >= 2 #True
# 0 >= 2 #False

# #Меньше или равно 
# 10 <= 5 #false
# 5 <= 10 #true
# 5 <= 5 #true

#строки и числа нельзя сравнивать, а строки между собой можно 

'+++++++++++++++++++++++++And, or, Not+++++++++++++++++++++++++'
#and  - и 
#or - или 
#not - отрицание 
 
# a = 5
# b = 6
 
# #True      #True --> TRUE
# a == 5 and b == 6 
# #True      #False --> FALSE
# a == 5 and b == 3
# #False     #False --> FALSE
# a > 10 and b < 2

#Возвратиться True, если справа и слева TRUE. 
#Если хотя бы с одной стороны будет False или двух, то возвратится False 

'OR'
a = 20 
b = 5

#True или True --> True
a == 20 or b > 1
#True или False --> True
a == 20 or b < 1
#False или True --> True
a > 100 or b == 5 
#False или False --> False 
a < 10 or b < 1 
# Если хотябы одна часть выражения будет True, то будет True

'NOT'

#not False - True
#not True - False 

# a = 5 
# not a < 10#False
# not a != 5#True

# not not not not not a != 10#True

# b = 10 
# c = 2
# not b<=10 or c < 10 #True

'++++++++++++++++Boolean Type+++++++++++++++++'
#Булевый тип данных имеет всего два значения: True либо False.

# bool(1) #True
# bool(0) #False
# bool(-123) #True

# '-5 ----------- 0 ----------- 5'
# bool('hello') #True
# bool(' ') #True
# bool('') #False

# bool(True)#True
# bool(False)#False

# bool([]) #False
# bool([[]]) #True
# bool([12,14[123,235]])#True

'++++++++++++++++++++=NONE TYPE++++++++++++++++++'
#None - неизменяемый тип данных с одним значением - None, который используется для обозначения отсутстивия значения.

# a = None 
# print(a)

# bool(None) #False
# bool('None') #True


'++++++++++++++++++++Условные операторы++++++++++++'
#Условные оператор - это конструкция. которая используется для того, чтобы при разных входных данных код работал по разному.

# if условие1:
#     тело
# '------------------'
# if условие1:
#     тело1 #будет выполнятся, если  условие1 - True
# else:
#     тело2 #тело 2 будется работать во всех других случаях.
# '-------------------------------------'
# if условие1: 
#     тело1
# elif условие2:
#     тело2

# '------------------------'
# if условие1: 
#     тело1
# elif условие2:
#     тело2
# else: 
#     тело3



# num1 = int(input('Введите первое число: '))
# num2 = int(input('ВВедите второе число: '))
# oper = input('введите оператор: ')
# if oper  == '+':
#     print(num1+num2)
# elif oper == '-':
#     print(num1-num2)
#     print(num1*num2)
# elif oper == '/':
#     print(num1/num2)
# elif oper == '**':
#     print(num1**num2)

"================Тернарный операторы================"
#only 'IF' and 'ELSE'
# telo1 if uslovlie else telo2

# a = 2
# res = a ** 2 if a > 0 else a - 2
# print(res)
a = int(input())
if a>0:
    res = a**2
else:
    a-2
print(res)