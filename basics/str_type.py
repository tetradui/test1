'+++++++++++++++++++++++++++++STRING++++++++++++++++++++++++++++++++'
#Строки - это неизменяемый тип данных, который предназначен для хранения текстов, 
#заключенного в одинарные или двойные кавычки

string1 = 'строка с одинарными ковычками'
string2 = "стркоа с двойными ковычками"
# string3 = 'неправильная строка"
string4 = " Don't " #внутри двойной ковычки одинарная, воспринимает как ковычку как часть текста
string5 = '''
    Многострочный текст в одинарных/двойных кавычках, тут можно ставить "любые" кавычки
    '''
string6 = 'hello' + 'world' #контатинация (плюс между слов)
# print (string6)

# string7 = 'А ' * 8 #умножение на число (АААААААА)
# print (string7)


'+++++++++++++++++++++++++++++ЭКРАНИЗАЦИЯ СТРОК+++++++++++++++++++++++++'
'\n'#перенос текста на новую строку
# print('hello\nworld')
#hello
#world

'\t'#табуляция
# print('kakadu\tkoala')

str1 = 'don\'t' #отображает кавычку ' в терминале (воспринимает ее как текст)
# print(str1)
str2 = "don\"t"
# print(str2)

str3 ='символ - \\'
# print (str3)

'\v'#перенос на новую строку со смещением вправо на длину предыдущей строки
str4 = 'sdfafasd\vclown\vsdfasd\vsdadga'
# print (str4)

'\r'#перенос каретки на начало строки
# str5 = 'makers bootcamp\rHI'
# print (str5)
# HIkers bootcamp

'+++++++++++++++++++++++ФОРМАТИВРОВАНИЕ СТРОК(ИНТЕРПОЛЯЦИЯ)++++++++++++++++++++++++++'

#1 f перед ковычкой 
# title = 'Samsung2'
# price = 100000

# format_2 = f'Мой телефон, {title} стоит {price} долларов'

# print (format_2)

#2 {} .format 
# strin2 = 'Название:{} Цена: {}'
# print (strin2.format('iPhone', 150)) #если две скобки(фигурные), то два обозначения, а то ошибка

#3
# string = 'Название: %s Цена: %s'
# print (string %('iphone', 150 ))


'++++++++++++++++++++++++МЕТОДЫ СТРОК+++++++++++++++++++++++++++++++++'
#Методы - это функции, которые относятся к опрделенному классу, к ним можно обращаться через точку.

# print (dir(str))

# string = 'Hello'
# print(string.upper())#MAKERS
# print(string.lower())#makers
# print(string.swapcase()) #делает большие маленькими, маленькие большими 

# print('heLlo world'.title())#hello world -> Hello World
# print('hello World'.capitalize())#hello World -> Hello world
# print(string.center(11, '='))#hello -> ===hello===
# print(string.count('l'))#hello (L) ->  2
# print(string.count(''))#hello -> 6(пустоы между буквами)
# print(string.startswith('a'))#hello (a) -> false, hello(h)->true
# print(string.startswith('H'))#False, (h)true
# print(string.endswith('d'))#false
# print(string.endswith('o'))#true

# #islower #isupper
# print('makers'.islower())#true 
# print('Makers'.islower())#false
# print('makers'.isupper())#false 
# print('MAKERS'.isupper())#true

# numbers = '1231asdf23'
# #isdigit() #isalpha() #isalnum() #isspace()
# print(numbers.isdigit())#true Проверка на числа
# print(numbers.isalpha())#false Проверка на буквы
# print(numbers.isalnum())#true провека на то, что является ли строка с числами или буквами, или все вместе, но не с символами
# print('\n\r'.isspace())#true проверка на неотображаемые символы

# #split
# words = 'hello, world, makers bootcamp'
# print(words.split())

# #lstrip() #rstrip() #strip()
# login = '    Salam'
# print(login.lstrip()) #Salam без пробелов слева
# print(login.rstrip()) #Salam без пробелов справа
# print(login.lstrip()) #Salam без пробелов

# #zfill() z-ноль fill - заполнить 
# fills = 'kutman'
# print(len(fills))#6
# print(fills.zfill(10))#0000kutman 
# #заполняет нулями, если в строке не хватает символов указанных в диапозоне
# '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
# #ljust(width, fillchar) #rjust(width, fillchar)
# justin = 'makers'
# print(justin.ljust(9, ')'))
# print(justin.rjust(9, ')'))

'++++++++++++++++++++++++++++++++++++++++РАЗДЕЛ ИНДЕКСА++++++++++++++++++++++++++++++++++++++++++++++'
#индекс - это порядковый номер элемента последовательност(символа в строке), (индексация начинатся с 0)

'h e l l o    w  o  r  l  d'
#0 1 2 3 4 5  6  7  8  9  10
# string = 'hello world'
# print(string[0])#h
# print(string[7])#o
# print(string[10])#d
# print(string[-1])#d

# #срезы - это подстрока(часть строки) string[start:end:step]
# string = 'hello world'
# print(string[3:5])#lo
# print(string[6:]) #world
# print(string[:])#hello world
# print(string[:5])#world
# print(string[::-1])#dlrow olleh
# print(string[::2])#hlowrd
# print(string[::3])#hlwl
# print(string[::4])#hor



