# ====1 ===
def funca():
    print('this is func a!')

def funcb():
    print('this is func b!')

def funcdef():
    print('this is func default!')

# 字典的value值是一个函数
switch1 = {
    'a':funca,
    'b':funcb
}

case = 'a'
switch1.get(case)()
# this is func a!

switch1.get('y',funcdef)()
# this is func default!


# =======2======
class switch2(object):
    def __init__(self,case):
        self.sw_ls = {
            'a':self.a,
            'b':self.__b
        }
        casefun = self.sw_ls.get(case,self.default)
        casefun()

    def a(self):
        print('this is a()')

    def __b(self):
        print('this is __b()')

    def default(self):
        print('this is default()')

switch2('a')    # this is a()
switch2('c')    # this is default()