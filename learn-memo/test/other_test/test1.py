# 对象存在但if判断不一定是True

class A1():
    pass

class A2():
    def __len__(self):
        return 0


print(bool(A1()))   # True
print(bool(A2()))   # False
print(bool(None))   # False

# =======

class A3():
    def __len__(self):
        print('this is len')
        return 1

print(bool(A3()))
# this is len
# True

class A4():
    def __bool__(self):
        print('this is bool')
        return False

    def __len__(self):
        print('this is len')
        return 1

print(bool(A4()))
# this is bool
# False
