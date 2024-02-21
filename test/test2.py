products = [
  {
    'title': 'Samsung S10', 
    'price': 800, 
    'count': 6, 
    'category': 'samsung'},
  {
    'title': 'iPhone 13 Pro', 
    'price': 1200, 
    'count': 9, 
    'category': 'apple'},
  {
    'title': 'Xiaomi Mi 10', 
    'price': 500, 
    'count': 2, 
    'category': 'xiaomi'},
  {
    'title': 'Samsung S9', 
    'price': 600, 
    'count': 4, 
    'category': 'samsung'},
  {
    'title': 'iPhone 11', 
    'price': 850, 
    'count': 1, 
    'category': 'apple'}
] 
def func23(list_,str_): 
    res = list()
    for i in list_: 
        if str_.lower() == i['category'].lower():
            res.append(i)
    return res
print(func23(products, 'apple'))

# def func21(a:list,b:str)->list: 
#     result=list() 
#     for i in a: 
#         if b.lower() == i['category'].lower(): 
#             result.append(i) 
#     return result
# print(func21(products, 'apple'))