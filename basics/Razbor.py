# nums_str = input('Введите числа через запятую без пробелов: ')
# list1 = nums_str.split(',')
# # list_.sort()
# list2 = sorted(list1)

# print(list2)


# number = input()
# list_ = number.split(',')
# tuple_ = tuple(number.split(','))
# print(list_)
# print(tuple_)

list_  = [1,'abc', 3,'1', 4,'xyz', 5,'pqr', 7,5,12]
res = 0
for i in list_:
    if type(i) == int or  i.isdigit():
        res = res + int(i)


   
print(res)