# 非闭包 - 旅行者行走
origin = 0

def go(step):
    global origin   # 需使用global声明全局变量
    new_pos = origin + step
    # 函数中定义了origin局部变量，函数使用origin将不会寻找全局变量origin
    # 上句引用origin将会找不到origin，global声明origin使用全局变量以解决问题
    origin = new_pos

    return origin

print(go(2))
print(go(3))
print(go(5))



# 闭包 - 旅行者行走

origin = 1

def factory(pos):
    def go(step):
        nonlocal pos    # 声明变量非当前局部变量，解决局部变量赋值被当成新变量的声明
        new_pos = pos + step
        pos = new_pos   # nonlocal声明后，此句python不会当成新变量的声明
        return new_pos
    return go

tourist = factory(origin)
tourist2 = factory(origin)

print(tourist(2))   # 3 = 1 + 2
print(tourist2(3))  # 4 = 1 + 3
print(tourist(5))   # 8 = 3 + 5