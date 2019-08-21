print('我是p1包的__init__.py模块')

__all__ = ['c1']

print('=================================')

for key in dir():
    exec('print("{}=%r"%{})'.format(key, key))

print('=================================')