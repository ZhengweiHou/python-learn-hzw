class Clazz:
    name = 'Clazz'
    age = 111

    def __init__(self, name1, age):
        self.name = name1
        self.age = age
        print(self.name)
        # print(name)  # 错误： NameError: name 'name' is not defind
        print(Clazz.name)  # Clazz

    def show_inst_name(self):
        print(self.name)

    @classmethod
    def show_cls_name(cls):
        print(cls.name)

    @staticmethod
    def show_static(x, y):
        '静态方法和和普通函数没有区别'
        print(x + y)


clazz = Clazz('张三', 15)

print(clazz.__dict__)
# {'name': '张三', 'age': 15}
print(clazz.__class__.__dict__)
# {'__module__': '__main__', 'name': 'Clazz', 'age': 111, ...}

clazz.show_inst_name()  # 张三
clazz.show_cls_name()  # Clazz

clazz.show_static(1, 2)  # 3
Clazz.show_static(3, 4)  # 7
