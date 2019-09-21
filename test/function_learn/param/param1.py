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
        exec('print("{}=",{})'.format(key, key))

a_dict = {'1':1,'2':2,'3':3}
func1('h','W',*'xyz',**a_dict)
# a= h
# b= W
# c= ('x', 'y', 'z')
# d= {'1': 1, '2': 2, '3': 3}

func1('h') # 默认值参数和可变参数，调用时可以不提供
# a= h
# b= 1
# c= ()
# d= {}



