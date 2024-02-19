# 1
# def sum_(x,y): 
#     return x+y
# print(sum_(2,3))

# or 

# list1 = [1,2]
# from functools import reduce
# def sum_(x,y): 
#     return x+y

# res = reduce(lambda x,y: x+y,list1 )
# print(res)



'====================================='
# 2
# def typee(x,y): 
#     return type(x), type(y)
# print(typee([],3))

# or 

# res = list(map(lambda y: type(y), ([],2)))
# print(res)

'====================================='
# 3
# def proizved(x): 
#     res = 1
#     for i in x: 
#         res = i * res
#     return res
# print(proizved([2,3,4,5,6]))

# or 

# from functools import reduce
# list2 = [2,3,4,5,6]
# i = 1
# res = reduce(lambda x,y: x*y, list2)
# print(res)

'====================================='
# 4 Напишите функцию, которая принимает строку и выводит количество гласных,
# согласных букв и остальных символов. Используйте только кириллические символы

# def checking(x): 

'====================================='
# 5 
# from functools import reduce
# names = ['Kutman', 'Lex', 'Katya', 'Jorobek']
# spi = (reduce(lambda x,y:x if len(x)>len(y) else y , names ))
# print(spi)

'====================================='
# 6) Дана глобальная переменная num со значением 3. Напишите функцию mul которая
# будет возвращать квадрат этой переменной и записывать результат в глобальную
# переменную num. Вызовите функцию три раза, и распечатайте переменную num.

# num = 3 
# def mul():
#     res = num**2
#     return (res)
# print(mul())
# print(mul())
# print(mul())

# print(num)
    

# a = 10 
# def func(a,b):
#     res = a+b
#     print(res)
#     print(locals())
# func(10,5)



'====================================='
# 8
list_ = [1,2,3,4,5,6]
result  = list(map(lambda x: x**2, list_))
print(result)