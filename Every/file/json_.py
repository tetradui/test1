'++++++++++++++++++++++++++++++++JSON++++++++++++++++++++++++++++'
#JavaScript Object Notation - 
# это универсальный формат, в котором мы можем хранить данные в типах данных, понятные почти для всех языков программирования 

import json 
# True -> true 
# json_data = "true"
# python_data = json.dumps(json_data)
# print(python_data)

# with open ('test.json', 'r') as file:
#     python_data = json.load(file)
# print(python_data)


# десериализация - перевод с json строки в python объекты
# loads - метод для десериализации с json строки
# load - метод для десериализации с json файла 


# python_data = None
# json_data = json.dumps(python_data)
# print(json_data)

# with open ('test.json', 'w') as file:
#     json.dump( json_data, file)


python_data = [1,2,3,4, None, 'makers', False, True]

with open ('test.json', 'w') as file:
    json.dump( python_data, file)
# сериализация - перевод python объетов в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериализации в json файл