# # dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# # for k,v in list(dict_.items()):
# #     for v1 in v.values(): 
# #         dict_[k] = v1
# # print(dict_)

# # dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# # for k,v in list(dict_.items()): 
# #     for v2 in v.values(): 
# #         dict_[k] = v2 
# # print(dict_)

# Дан словарь dict1. 
# Создайте словарь dict2, с ключами как в словаре dict1,
# а значениями пусть будут произведение чисел внутренних словарей

dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}

for k,v in (dict1.items()):
    res = 1
    for v1 in v.values():
        res = res * v1
        dict2[k] = res
print(dict2)

