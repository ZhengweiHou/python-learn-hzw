# 装饰器方法
def decorator_func1(original_func):

    def wrapper_func(*args,**kwargs):
        print("{}执行：{}函数，参数：".format('wrapper_func', original_func.__name__),*args,*kwargs)
        return original_func(*args,**kwargs)

    return wrapper_func

@decorator_func1
def display1():
    print("我是display1")

@decorator_func1
def display2(arg1):
    print("我是display2",arg1)

display1()
display2(123)


# 装饰器类
class decorator_class1:
    def __init__(self,original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print('执行{}前执行{}'.format(self.original_func.__name__,'decorator_class1.__call__()'))
        return self.original_func(*args,**kwargs)


@decorator_class1
def display3():
    print("我是display3")

@decorator_class1
def display4(arg1):
    print("我是display4",arg1)

display3()
display4(222)


