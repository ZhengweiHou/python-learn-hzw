# 装饰器类
class logit(object):
    def __init__(self,logfile='out.log'):
        self.logfile=logfile

    def __call__(self, func):

        def wrap_func(*args,**kwargs):
            print('记录日志到：',self.logfile,',msg:',func.__name__+' was called')
            return func(*args, **kwargs)

        return wrap_func

@logit()
def my_func1():
    print('I am my_func1')

my_func1()
# 记录日志到： out.log ,msg: my_func1 was called
# I am my_func1

@logit(logfile='hzw.log')
def my_func2():
    print('I am my_func2')

my_func2()
# 记录日志到： hzw.log ,msg: my_func2 was called
# I am my_func2