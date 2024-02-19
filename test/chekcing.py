def collect_all_possibles(list_: list, num: int) -> list: 
    result = [] 
    for x in list_: 
        try: 
            result.append(x * num) 
            result.append(x + num) 
            result.append(x - num) 
            result.append(x ** num) 
            result.append(x // num) 
        except TypeError: 
            pass 
    return result