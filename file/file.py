'+++++++++++++++Module & package++++++++++++++++++++'
#.py - module
# more modules - package

'++++++++++++++File++++++++++++++++++'
# open() - функция, которая открывает файл в опредленном режиме

# r - read() (только для чтения)
# w - write() (для записи, каждый раз файл очищается)
# a - append() (только для дозаписи, добавляется в конец)
# x - создает файл, но если файл с таким же именем существует, то выйдет ошибка 


'--------------------------------read-------------------------------------'
# file = open('test1.txt', 'r')
# # # print(dir(file))
# # print(file.writable()) #false
# # print(file.readable()) #true
# # print(file.read()) # read file
# # file.seek(0) # возвращает на указанный индекс
# # print(file.read(10)) 

# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readlines()) 
# 'read - str, readline -> str, readlines: List[str]'
# file.close()

'-----------------------------write--------------------------------------'
# file = open('test1.txt','w')
# # file.write('Makers\nHello World\n')
# file.writelines(['HELLO world\n', 'makers\n'])
# 'write(str), writeline(list[str,str])'
# file.close()

'----------------------------append--------------------------------------'
# Добавляет в файл текст, не удаляю предыдущие записи
# file = open('test1.txt', 'a')
# file.write('py33\n')
# file.write('py32\n')
 
'=---------------------------Контекстный менеджер----------------------='
# with

with open('test1.txt') as f:
    print(f.read())
    
print(f.closed) # True - файл закрылся

