# 函数装饰器
print('==函数装饰器==')

'''
==第一个装饰器==
'''
def func_decorator1(func):
    def wrap_func1():
        print(func.__name__,'befor')
        func()
        print(func.__name__,'after')

    return wrap_func1

@func_decorator1
def my_func_1():
    print('I am func_1')

print(my_func_1.__name__,my_func_1())
# 输出：
# my_func_1 befor
# I am func_1
# my_func_1 after
# wrap_func1 None

# 注意： func_1.__name__变成了wrap_func1


# ==被装饰函数有参数和返回值==
# 1. 使用@wraps注解限定被装饰函数的name等属性
# 2. 装饰函数使用可变参数传递被装饰函数的参数
from functools import wraps

def func_decorator2(func):
    @wraps(func)        # 解决上面被装饰函数name改变问题
    def wrap_func2(*args, **kwargs):
        print(func.__name__,'befor')
        result = func(*args, **kwargs)
        print(func.__name__,'after')
        return result

    return wrap_func2

@func_decorator2
def my_func_2(msg='def msg'):
    print('I am func_2, msg:',msg)
    return '='+msg+'='

print(my_func_2.__name__,my_func_2('HZW'))
# 输出：
# my_func_2 befor
# I am func_2, msg: HZW
# my_func_2 after
# my_func_2 =HZW=

# 注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。


# ==带参数的装饰器==
def logit(level='INFO',logfile='out.log'):
    def log_decorator(func):
        @wraps(func)
        def log_wrap(*args,**kwargs):
            print('LOG:[', level, '], outfile:', logfile, ',args:', args, kwargs)
            return func(*args,**kwargs)
        return log_wrap
    return log_decorator

@logit()
def my_func3(arg1=1, arg2=2):
    print('I am my_func3,',arg1, arg2)

@logit(level='DEBUG', logfile='hzw.log')
def my_func4(arg1=1, arg2=2):
    print('I am my_func4,',arg1, arg2)

my_func3('a')
# LOG:[ INFO ], outfile: out.log ,args: ('a',) {}
# I am my_func3, a 2

my_func4()
# LOG:[ DEBUG ], outfile: hzw.log ,args: () {}
# I am my_func4, 1 2



