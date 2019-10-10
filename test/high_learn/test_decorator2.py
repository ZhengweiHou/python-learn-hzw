from functools import wraps

def a_decorator1(func):

    @wraps(func)
    def a_dec_fun(*args,**kwargs):

        print('*args:', args, '**kwargs', kwargs)
        print(func.__name__,'befor1')
        result = func(*args,**kwargs)
        print(func.__name__,'after1')

        return result

    return a_dec_fun

def a_decorator2(func):

    @wraps(func)
    def a_dec_fun(*args,**kwargs):

        print('*args:', args, '**kwargs', kwargs)
        print(func.__name__,'befor2')
        result = func(*args,**kwargs)
        print(func.__name__,'after2')

        return result

    return a_dec_fun

@a_decorator1
@a_decorator2
def a_func(message):
    print(message)
    return message + 1000

print(a_func(message=1231))