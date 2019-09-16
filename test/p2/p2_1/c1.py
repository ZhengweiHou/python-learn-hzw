'''
我是注释
'''


# a='我是c1模块的a'
# b='我是c1模块的b'

a='我是'+__name__+'的a'
b='我是'+__name__+'的b'


from ..c2 import a
print(a)




