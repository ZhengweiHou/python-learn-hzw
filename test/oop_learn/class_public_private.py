

class Student:
    name = ''
    __weight = 0

    def __init__(self, name, weight, age):
        self.name = name
        self.__weight = weight
        self.__age = age  # 构造器中可以添加私有变量

    def __private_func(self):
        print('__private_func')

    def public_func(self):
        print('public_func')
        self.__private_func()
        self.__hehe = 'hehe'  # 方法中可以为实例添加私有变量


s1 = Student('张三', 50, 11)

s1.__age = 22  # 不可动态修改私有变量，此句会为s1添加一个变量__age,而不会修改_Student__age的值

s1.public_func()

print(vars(s1))
print(s1.__dict__)
# {'name': '张三', '_Student__weight': 50, '_Student__age': 11, '__age': 22, '_Student__hehe': 'hehe'}

print(dir(s1))
# ['_Student__age', '_Student__hehe', '_Student__private_func', '_Student__weight', '__age', 'name', 'public_func', ...]


print(s1._Student__weight)  # 可以改名后的变量名访问

s1._Student__private_func()  # 可以正常访问改名后的私有方法
