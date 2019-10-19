# =======if=======

num=9

#----------------------
if num < 5 :
    print('小于5')
elif num == 5 :
    print('等于5')
else:
    print('大于5')

#----------------------
if not num == 9:
    print('不等于9')
else:
    print('等于9')



# =======for=======
l=[]
for a in range(10):
    if a%2:
        l.append(a)
print(l)


print(
    [b for b in range(10) if not b%2]
)

