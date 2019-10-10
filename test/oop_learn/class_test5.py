class A(object):
    def __new__(cls, *args, **kwargs):
        print('__new__',args,kwargs)

    def __init__(self):
        print('__init__')


A()
A(1,2,3,a=9)