def func13(a): 
    dict_={}
    for i in a: 
        dict_[i] = a.count(i)
    return dict_
print(func13('hello'))