# ==== iterator ====
print('==== iterator ====')
# 可迭代对象
a = (1,2,3,4)   # tuple
b = [1,2,3,4]   # list
c = 'abcd'      # str

tmp1 = [i for i in a]
tmp2 = (i for i in b)   # 小括号包装的列表推导式，得到的将是一个生成器对象
tmp3 = {i for i in c}

print(tmp1) # [1, 2, 3, 4]
print(tmp2) # <generator object <genexpr> at 0x7f6abe714750>
print(tmp3) # {'a', 'b', 'c', 'd'}


# 迭代器
class codes():
    def __init__(self):
        self.code_list = ['Java','Python','ruby']
        self.cur_index = 0

    def __iter__(self):
        print("iter",end=' ')
        return self # 返回一个迭代器

    def __next__(self):
        print("next_1", end=' ')

        if self.cur_index >= len(self.code_list):
            # 当遍历位置超过列表时抛出StopIteration异常
            print("next_e")
            raise StopIteration()

        # print("next2",end=' ')

        result = self.code_list[self.cur_index]
        self.cur_index += 1
        return result

code1 = codes()

print(code1.__next__())
# next_1 Java

for code in code1:
    print(code)
# iter next_1 Java
# next_1 Python
# next_1 ruby
# next_1 next_e

for code in code1:
    print(code)
# iter next_1 next_e


# ======generator======
print('======generator======')

def generator_num(max):
    n = 0
    while n <= max:
        n += 1
        yield n # yield 返回生成器每次产生的对象, yield不会中断函数和return不同

gen1 = generator_num(100)

print(type(gen1))   # <class 'generator'>
# 使用next()获取生成器的下一个元素
print(next(gen1))   # 1
print([i for i in gen1 if i%10==0]) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



# 列表推导式生成生成器
gen2 = (i for i in range(101,201))
print(type(gen2))   # <class 'generator'>
print(next(gen2))   # 101
print([i for i in gen2 if i%10==0]) # [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
print(next(gen2))   # 再次next生成器会抛异常 StopIteration







