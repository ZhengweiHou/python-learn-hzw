class P:
    def __init__(self, name):
        print(__class__, id(self), self.__class__)
        self.name = name
        self.name2 = name

    def run(self):
        print(self.name, 'run....')


class M:
    def __init__(self, name):
        print(__class__, id(self), self.__class__)
        self.name = name

    def jump(self):
        print(self.name, 'jump....')


class S(P, M):
    name = '11111111'

    def __init__(self, name):
        self.name = name
        super().__init__("haha")
        print(__class__, id(self), self.__class__)


s = S('hyc')
s.run()
s.jump()

print(s.__dict__)
# del s.name3
delattr(s, 'name')
print(s.__dict__)

# del s.__class__.name

print(s.__class__.__dict__)


class Clazz:

    name = 'Clazz'
    age = 111

    def __init__(self, name, age):
        self.name = name
        self.age = age

clazz = Clazz('张三', 15)

print(clazz.__dict__)
# {'name': '张三', 'age': 15}
print(clazz.__class__.__dict__)
# {'__module__': '__main__', 'name': 'Clazz', 'age': 111, ...}
