from functools import reduce

result = reduce(lambda x,y:x+y, range(5))
print(result) # 10 = 0 + 1 + 2 + 3 + 4

print(list(range(5)))