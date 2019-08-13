'''
测试程序
'''

username = 'hzw'
password = '123456'

print('please input username >', end='')
username_temp = input()

print('please input passwort >', end='')
password_temp = input()

if username_temp == username and password_temp == password:
    print('you are right!!')
else:
    print('you are lose!!')