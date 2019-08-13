a = input('input>')

if a == 1:
    print('is int 1')
elif a == '1':
    print('is str \'1\'')
elif a == 2:
    print('is int 2')
else:
    print('a is %r' % a)
