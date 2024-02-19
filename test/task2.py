# def is_palindrome(a):
#     if a==a[::-1] or a == reversed(a):
#        return(True)
#     else:
#         return(False)
# print(is_palindrome(''))

def is_palindrome(a):
    if a==a[::-1]:
       return(True)
    else:
        return(False)
print(is_palindrome('Mom'.lower()))



