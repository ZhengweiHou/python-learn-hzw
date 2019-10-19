# Python杂记
## 前言
<font color="red">Python和其他语言一样，知识点是很多的，本章意于记录一些杂乱的知识点，便于自身进步和回顾。</font>


## 1. 用字典代替switch
> Python没有java中的switch关键字，Python可以使用字典实现其他语言的switch功能
``` python
def funca():
    print('this is func a!')

def funcb():
    print('this is func b!')

def funcdef():
    print('this is func default!')

# 字典的value值是一个函数
switch1 = {
    'a':funca,
    'b':funcb
}

case = 'a'
switch1.get(case)()
# this is func a!

switch1.get('y',funcdef)()
# this is func default!
```

## 2. 集合推导式
- 普通用法
``` python
a = list(range(10))

b = [i for i in a if i%2 ]
print(type(b),b) # <class 'list'> [1, 3, 5, 7, 9]

c = {i for i in a if i%2}
print(type(c),c) # <class 'set'> {1, 3, 5, 7, 9}
```

- 字典列表推导式
``` python
dict1={
    'a':1, 'b':2, 'c':3
}

# dict不可被直接遍历, dict.items()获取遍历对象后使用
dict2 = {value:key for key,value in dict1.items()}
print(dict2)    # {1: 'a', 2: 'b', 3: 'c'}
```

## 3. iterator与generator
### 迭代器 iterator
1. iterable 可迭代对象  
    指可被for in遍历的对象，list、tuple、set等都是可迭代对象。
    ``` python
    # 可迭代对象
    a = (1,2,3,4)   # tuple
    b = [1,2,3,4]   # list
    c = 'abcd'      # str
    
    tmp1 = [i for i in a]
    tmp2 = (i for i in b)   # 小括号包装的列表推导式，得到的将是一个生成器对象
    tmp3 = {i for i in c}
    
    print(tmp1) # [1, 2, 3, 4]
    print(tmp2) # <generator object <genexpr> at 0x7f6abe714750>
    print(tmp3) # {'a', 'b', 'c', 'd'}
    ```
2. 迭代器类 iterator   
    - 迭代器是一个类，自定义类可以继承itedrator变成一个迭代器类。  
    - 迭代器关键方法：   
        - `__iter__()`  
            承诺：组织并返回迭代器
        - `__next__()`  
            承诺：返回每次遍历的元素，列表已遍历完，抛出异常
    - 迭代器实例后只能遍历一次  
    **例：**
    ``` python
    # 迭代器
    class codes():
        def __init__(self):
            self.code_list = ['Java','Python','ruby']
            self.cur_index = 0
    
        def __iter__(self):
            print("iter",end=' ')
            return self # 返回一个迭代器
    
        def __next__(self):
            print("next_1", end=' ')
    
            if self.cur_index >= len(self.code_list):
                # 当遍历位置超过列表时抛出StopIteration异常
                print("next_e")
                raise StopIteration()
    
            # print("next2",end=' ')
    
            result = self.code_list[self.cur_index]
            self.cur_index += 1
            return result
    
    code1 = codes()
    
    print(code1.__next__())
    # next_1 Java
    
    for code in code1:
        print(code)
    # iter next_1 Java
    # next_1 Python
    # next_1 ruby
    # next_1 next_e
    
    for code in code1:
        print(code)
    # iter next_1 next_e
    ```
    > 第一次遍历正常第二次遍历时cur_index已经超过list长度，__next__直接返回异常结束遍历了



### 生成器 generator
- yield 生成器使用yield返回生成元素  
    不会中断生成器函数
- 生成器遍历完后再次遍历或取值会抛出StopIteration异常
``` python
def generator_num(max):
    n = 0
    while n <= max:
        n += 1
        yield n # yield 返回生成器每次产生的对象, yield不会中断函数和return不同

gen1 = generator_num(100)

print(type(gen1))   # <class 'generator'>
# 使用next()获取生成器的下一个元素
print(next(gen1))   # 1
print([i for i in gen1 if i%10==0]) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



# 列表推导式生成生成器
gen2 = (i for i in range(101,201))
print(type(gen2))   # <class 'generator'>
print(next(gen2))   # 101
print([i for i in gen2 if i%10==0]) # [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
print(next(gen2))   # 再次next生成器会抛异常 StopIteration
```


### 对象存在但if判断不一定是True
不可以认为对象存在时if判断就是True
``` python

class A1():
    pass

class A2():
    def __len__(self):
        return 0


print(bool(A1()))   # True
print(bool(A2()))   # False
print(bool(None))   # False
```

if判断对象是否为True和两个内置方法有关：
- `__bool__(self)`
- `__len__(self)`
``` python
class A3():
    def __len__(self):
        print('this is len')
        return 1

print(bool(A3()))
# this is len
# True

class A4():
    def __bool__(self):
        print('this is bool')
        return False

    def __len__(self):
        print('this is len')
        return 1

print(bool(A4()))
# this is bool
# False
```


### 装饰器的副作用
被装饰函数name和注释被替换成装饰闭包函数    
    >使用functools wraps装饰器解决