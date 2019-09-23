print('=========函数调用=========')

# & 序列前加*会解包序列
# & **dict 会将字典解包为 key1=value1,key2=value2 的形式 （可作为关键字参数调用函数）
print('=========解包序列=========')
print(*'abc') # a b c

a_list=[1,2,3]
print(*a_list)  # 1 2 3

a_dict = {'a':1,'b':2,'c':3}
print(*a_dict) # a b c



def func1(a,b,c):
    print(a,b,c)

a_list=[1,2,3]
func1(*a_list)  #相当于 func1(1,2,3)
func1(*'123')
func1(1,2,3)

a_dict = {'a':1,'b':2,'c':3}
func1(**a_dict)  #相当于 func1(a=1,b=2,c=3)
func1(a=1,b=2,c=3)


