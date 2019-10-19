
# 闭包 = 函数 + 环境变量
#函数和变量构成闭包时，闭包中变量不会被外部影响
a = 20
b = 30

def out_fun():
    a = 2
    b = 3
    def in_fun(x):      # 1. 外函数内定义了一个内函数
        # b = 10        # 此时b属于内函数的局部变量，则b不会成为闭包环境变量
        return a*b*x    # 2. 在内函数里引用了外函数临时变量a、b，a、b变量才会进入闭包里

    return in_fun       # 3. 外函数返回子函数的引用

f = out_fun()
print(f.__closure__)    # __closure__ ：闭包中包含的环境变量
print(f.__closure__[0].cell_contents)   # 闭包第一个变量的值：a
print(f(2))




