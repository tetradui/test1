# dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values = sorted(dict1.values())
# sorted_dict = {}
# for i in sorted_values:
#     for k in dict1.keys():
#         if dict1[k] == i:
#             sorted_dict[k] = dict1[k]
#             break
# print(sorted_dict)


# # dict1 = {1: 1, 2: 9, 3: 4}
# # sorted_values = sorted(dict1.values()) # Sort the values
# # sorted_dict = {}

# # for i in sorted_values:
# #     for k in dict1.keys():
# #         if dict1[k] == i:
# #             sorted_dict[k] = dict1[k]
# #             break

# # print(sorted_dict)
a = {0, 1, 2, 3, 34, 5, 8, 13}
b = {1, 2, 34}
if a.issuperset(b):
    print('Надмножество! ')