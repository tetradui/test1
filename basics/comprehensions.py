'=================Compreshensions================'
# генератор, с помощью которого мы можем создавать последовательности используя цикл for в одну строку

# элемент for элемент in последовательность 
# элемент for элемент in последовательность if фильтр
# элемент1 if условие1  else элемент2 for элемент in последовательность 

# compr_ = [i if i % 2 == 0 else 'elem' for i in range(10)]
# print(compr_)

# compr_1 = []
# for i in range(10):
#     if i % 2 == 0:
#         compr_1.append(i)
#     else:
#         compr_1.append('elem')
# print(compr_1)

# list_ = [12, None, 'hi', 123, 1, 6, 2, True, 0, False]


# new_list = [i for i in list_ if i == True]
# print(new_list)


# new_list2 = [i if  bool(i) else 0 for i in list_]
# print(new_list2)

# new_list = []
# for i in list_:
#     if bool(i):
#         new_list.append(i)
#     else: 
#         new_list.append(0)

# print(new_list)





# list_ = [12,3,0,7,34,9,7]
# # new_list = ['четное 'if i % 2 == 0 else 'нечетное' for i in list_]
# # print(new_list)

# list1 = [1, 'Hi', 123, True, 'Makers', False]
# # list2 = []
# # for i in list1:
# #     if type(i) == str:
# #         list2.append(i)
# #     print(list2)

# new_list = [i**2 for i in list1 if type(i) == int]
# print(new_list)

'++++++++++++++++++++++++++++Виды comprehensions+++++++++++++++++++++'
# list comprehension -> []
# dict comprehension -> {:}
# set  comprehension -> {}

#comprehension генератор -> ()

'DICT COPREHENSIONS'
# {1:1, 2:4, 3:9, 4:16}

# dict_ = {i:i**2 for i in range(1,5)}
# print(dict_)

# dict_ = {'a':1, 'b':2, 'c':3}
# new_dict_ = {v:k for k,v in dict_.items()} # {1: 'a', 2: 'b', 3: 'c'}
# print(new_dict_)

# new_dict_2 = {v**2:v for v in dict_.values() if v % 2 == 0}
# print(new_dict_2) 


'SET COMPREHENSION'

# set_ = {i for i in range(11) if i % 2 == 0}
# print(set_)

# set1 = {12,34,35,True,345,'hi',4,'hello',6,5,}
# set2 = {i.upper() for i in set1 if type(i)==str}
# print(set2)

#два одинаковых значени в SET не может быть 

'++++++++++++++++++++++++++++++++++++++++++Вложенные comprehension++++++++++++++++++++++++++++++++++++++++++++'
#Создайте словарь, где ключами будут числа от 1 до 5, а значениями - списки с числами от 1 до этого числа)
# dict1_ = {}
# for i in range(1,6):
#     key = i
#     values = [j for j  in range(1, i+1)]
#     dict1_[key] = values 
# print(dict1_)


# dict_ = {i:[j for j in range(1, i+1)] for i in range(1,6)}
# print(dict_)
#запутанный способ
'------------------------------------------'

print([['hello world']*5]*10)
