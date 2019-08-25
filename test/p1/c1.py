'''
我是注释
'''


a='我是c1模块的a'
b='我是c1模块的b'

for key in dir():
    exec('print("{}=%r"%{})'.format(key, key))



