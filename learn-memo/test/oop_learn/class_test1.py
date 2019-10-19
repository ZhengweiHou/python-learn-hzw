class A:
    attr1 = 'hello'
    def __init__(self):
        print('A.__init__')

    def asay(self):
        print("asay", self.attr1)


class B(object):
    def __init__(self):
        print('B.__init__')

    def bsay(self, arg):
        print("bsay", arg)


class I(A, B):
    'I\'m I\'s document!!'
    def __init__(self):
        super().__init__()          #调用A.__init__()
        super(I, self).__init__()   #调用A.__init__()
        B.__init__(self)            #调用B.__init__()
    pass



i = I()
i.asay()
i.bsay('hello')

print(I.__doc__)
print(i.__doc__)

print(getattr(i, 'attr1'))
