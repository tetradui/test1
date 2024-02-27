# В текстовом файле посчитать количество строк, а также для каждой отдельной
# строки определить количество в ней символов и слов.

with open('cv.txt') as file: 
    len_ = file.readlines()
    num_str = (len(len_))
    print(num_str, 'количество строк\n')

with open('cv.txt') as file: 
    i = file.readlines()
    for count in i: 
        each_str = (len(count))
        print(each_str, 'количество символов')
 
