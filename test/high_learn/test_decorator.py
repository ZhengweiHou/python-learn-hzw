# 1.
def decorator_func(func):
    def wrap_func(*args, **kwargs):
        print('decorator do some thing..')
        return func(*args, **kwargs)
    return wrap_func

@decorator_func
def func1(arg):
    print("func1",arg)

func1(5)

# 等价于

func1 = decorator_func(func1)
func1(5)