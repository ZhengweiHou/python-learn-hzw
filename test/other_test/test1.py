def func(*args):
    print(args)
    print(*args)
    a,*args = args

    print(a)
    print(args)

func(1,2,3,4)




