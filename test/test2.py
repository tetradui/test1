list_ = ['a', 'n', 'n', 'a']
def palindrom(x): 
    if x == reversed(x):
        return "YES"
res = map(palindrom, list_)
print(res)