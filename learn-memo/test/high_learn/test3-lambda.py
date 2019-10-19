# 匿名函数

def add(x,y):
    return x + y
print(add(1,2))

add = lambda x,y: x + y
print(add(1,2))

(x,y)=(10,20)
f = lambda : (x,y,print(x + y))
print(f())


# 三元表达式
x = 11
y = 22

print(x if x > y else y)

