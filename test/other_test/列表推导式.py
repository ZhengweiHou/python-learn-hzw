# 列表推导式
a = list(range(10))

b = [i for i in a if i%2 ]
print(type(b),b) # <class 'list'> [1, 3, 5, 7, 9]

c = {i for i in a if i%2}
print(type(c),c) # <class 'set'> {1, 3, 5, 7, 9}


# 字典列表推导式

dict1={
    'a':1, 'b':2, 'c':3
}

# dict不可被直接遍历, dict.items()获取遍历对象后使用
dict2 = {value:key for key,value in dict1.items()}
print(dict2)    # {1: 'a', 2: 'b', 3: 'c'}

print(type((1,2)))

