users = {'Tim':'1234', 'Alex':'qwert', 'Sadyr':'654' } 
def validate_password(func): 
    def wrapper(username, password): 
        if username not in users: 
            print("Username is not defined") 
            return 
        elif users[username] != password: 
            print("Password is invalid") 
            return 
        else: 
            return func(username, password) 
    return wrapper 

@validate_password 
def login(username, password): 
    print(f'Welcome, {username}') 
login('Tim','1234')
