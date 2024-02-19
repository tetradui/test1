'===================Циклы==================='
# циклы - это блок кода, который отрабатывает несколько раз 

'итерируемый объект - это какая-та последовательность, которую мы можем перебрать. Например: [1,2,3], - list, "hello world" - str, {"a":1, "b":2} - dict, (1,2,3,4,123,True) - tuple '
"""Итерация - процесс перебора итерируемого объекта"""


# 1. for - цикл, который работает с итерируемым объектом, цикл заканчивает свою работу, когда он доходит до последнего элемента итерируемого объекта

# 2. while - цикл, который работает до тех пор пока условия верное 

'FOR'
# list_ = [1, True, 'hello', 0, 123]
# for elem in list_:
#     if elem != 0:
#         print(elem)

'WHILE'

# count = 0
# while count <= 10:#True
#     print(count) 
#     count = count + 2

'++++++++++++++Ключевые слова в циклах+++++++++++++'
# break - это оператор, который останавливает работу цикла(Ломает)
# continue - оператор, который пропускает итерацию (продолжает с другой итерации )

# range(start , end, step) - это генератор последовательности от start до end(не включительно)
# print(list(range(1, 11, 2)))
# print(list(range(10, 1, -1)))

# for i in range(0,21):
#     if i==10 or i==5:
#         continue
#     print(i)


# for i in ['1','2','3', 'world ']:
#     if i.isdigit():
#         print(int(i))
#     elif i.isalpha():
#         print('Я не могу перевести буквы в числа')
#         break
#     else:
#         print("я нашел символы")
    
# count = 0
# password = input('Enter password: ')
# while True:
#     print(count)
#     if str(count) == password:
#         print("It's your password: ", password)
#         break
#     count += 1     #count = count + 1

# count = 0
# while True:
#     if count > 1:
#         continue
  
#     print(count)
#     count += 1
# else:
#     print('hi')
    

# else в  цикле работает тогда, когда условие цикла становится false, если же сработал break, то else не сработает.