def foo(): 
    var = 'переменная foo' 
    print('переменная в foo: ', var) 
def bar(): 
    global var 
    var = 'переменная bar' 
bar() 
foo() 
print('переменная в foo: ', var)