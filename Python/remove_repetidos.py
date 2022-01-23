def remove_repetidos(lista):
    i = len(lista)
    new_list = []
    for item in lista:
        if item in lista and item not in new_list:
            new_list.append(item)
    
    return sorted(new_list)


