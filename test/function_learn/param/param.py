print('=========函数定义=========')
# 必选参数
print('=========必选参数=========')
def func1(a,b,c):
    print(a,b,c)

func1(1,2,3)


# 默认参数 - 形参列表中给默认值
print('=========默认参数=========')
def func1(a,b=2,c=3):
    print(a, b, c)

func1('h','w')


# 可变形参
print('=========函数定义 可变形参  =========')
def func1(*a):  # 定义函数时形参前加*,会将传入参数封包为元组tuple
    print(a)

func1(1,2)

a_list=['h','w','z']
func1(a_list)
func1(*a_list)


def func1(**a): # 定义函数时形参前加**,会将传入参数封包为字典dict
    print(type(a),a)

func1(a=1,b=2)

a_dict = {'a':1,'b':2,'c':3}
func1(**a_dict)


# 形参定义顺序
print('=========形参定义顺序=========')
def func1(a,b=1,*c,**d):
    for key in dir():
        exec('print("[{}",type({}),{},end="],")'.format(key, key, key))

a_dict = {'1':1,'2':2,'3':3}
func1('h','W',*'xyz',**a_dict)
# [a <class 'str'> h],[b <class 'str'> W],[c <class 'tuple'> ('x', 'y', 'z')],[d <class 'dict'> {'1': 1, '2': 2, '3': 3}],

func1('h') # 默认值参数和可变参数，调用时可以不提供
# [a <class 'str'> h],[b <class 'int'> 1],[c <class 'tuple'> ()],[d <class 'dict'> {}],



# & 序列前加*会解包序列
# & **dict 会将字典解包为 key1=value1,key2=value2 的形式 （可作为关键字参数调用函数）
print('=========解包序列=========')
print(*'abc') # a b c

a_list=[1,2,3]
print(*a_list)  # 1 2 3

a_dict = {'a':1,'b':2,'c':3}
print(*a_dict) # a b c


def func1(a,b,c):
    print(a,b,c)

a_list=[1,2,3]
func1(*a_list)  #相当于 func1(1,2,3)
func1(*'123')
func1(1,2,3)
# 1 2 3

a_dict = {'a':1,'b':2,'c':3}
func1(**a_dict)  #相当于 func1(a=1,b=2,c=3)
func1(a=1,b=2,c=3)
# 1 2 3

a_dict2 = {'a':1,'c':3}
func1(**a_dict2,b=4) # 1 4 3
func1(*'12',3) # 1 2 3
func1(3,*'12') # 3 2 1


print('=========包裹参数=========')
def func1(*a):   # 调用函数会将传入参数包裹成tuple
    for key in dir():
        exec('print("[{}",type({}),{},end="],")'.format(key, key, key))
        print()

func1(1,2,3)    # [a <class 'tuple'> (1, 2, 3)],


def func1(a,**b):   # 调用函数会将传入参数包裹成dict
    for key in dir():
        exec('print("[{}",type({}),{},end="],")'.format(key, key, key))
        print()

func1(a=1,y=2,z=3)  # [a <class 'int'> 1],[b <class 'dict'> {'y': 2, 'z': 3}],


def func(a,b,c,*d,**e):
    for key in dir():
        exec('print("[{}",{},end="],")'.format(key, key))

dict1={'x':6,'y':7}
func(1,*(2,3,4),5,**dict1) # [a 1],[b 2],[c 3],[d (4, 5)],[e {'x': 6, 'y': 7}],
# 等价于=》
func(1,2,3,4,5,x=6,y=7)    # [a 1],[b 2],[c 3],[d (4, 5)],[e {'x': 6, 'y': 7}],