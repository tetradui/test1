#Список - изменяемый тип данных

# string = 'hello'
# res = list(string)
# print(string.split())
# print(res)


# list_ = []
# list_ = list()
# list_ = [2]*10
# print(list_)

'+++++++++++++++++++++++++Методы списков++++++++++++++++++++++++++++'
#append - добавление элементы в конец
list_=[]
list_.append(True)
list_.append('subwey serfers')
list_.append(123)
list_.append([1,2,3])
# print(list_)

#pop - удаляется элементы из списка по индексу и возвращает удаленный элемент, если не передать индекс в скобки, то удалит последний элемент
list1 = ['asdf',5,5,5,True,5,5,5,None,5,5]
re_elem = list1.pop(6)
# print(re_elem)
# print(list1)

# remove - удаление элемента из списка по значению 
list2 = [123,23,3426,7543, 'kutman', True, False]
list2.remove(23)
# print(list2)

# count - метод, который считает количество элементов в списке
list3=[1, 2, False, 3, 'Clown', 4, 5, 6, True, None,0,0,0,0,0]
# print(list3.count(0))


# index - возвращает индекс первого вхождения указанного элемента
list3 = [12,3,3,3,'hi',None]
index_=list3.index('hi')
# print(index_)

# insert - добавляет элемент в список по указанному индексу
list4 = [123,234,1234,45,543,'dfg',True, False]
list4.insert(2, 'makers')#2 это индекс
# print(list4)

# extend - добавляет элементЫ списка в другой список
list0 = [0,0,0]
listSec = [1,2,3]

list0.extend(listSec)
# print(list0)

# reverse - расставляет элементы в обратоном порядке 
list10 = [123,2134,435,[1233,'erwwer',True],4563,4152]
# print(list10)
list10.reverse()
# print(list10)

# sort - сортирует список состоящий из элементов одного типа данных
list_sort = [2,3434,52,34223,1231,2,523]
list_sort.sort()
# print(list_sort)

list_sort2 = ['hi', 'makers', 'asd', 'qwerty']
list_sort2.sort(key = len,reverse=True)#['makers', 'qwerty', 'asd', 'hi']
# print(list_sort2)

vowels = ["a", "e", "i", "o", "u"]
vowels_str = ",".join(vowels)
print("Строка гласных:", vowels_str)

# COPY AND DEEPCOPY what is that?

'++++++++++++++++++++++++++Tuple+++++++++++++++++++++++++++'
# Кортеж - это упорядочный, неизменяемый, итерируемый тип данных, литерлы это (,) (ТОЛЬКО ДВА МЕТОДА)

tuple_ = (1, 2, 3, 4, 5,True, False, None)# Только два метода
tuple_.count(1)
# tuple_.index(2)
# print(tuple_.count(1))

