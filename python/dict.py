def Merge(dict1, dict2):
    # dict2合并了dict1
    return (dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}
Merge(dict1,dict2)
print(dict2)
