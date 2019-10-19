
# e.g.1
list1 = [1,5,6,2,7]
list2 = [9,0,8,3,4]

result = map((lambda x,y:x if x > y else y),list1,list2)

print(list(result))

# e.g.2
result = []
for x in range(5):
    result.append(x ** 2)
print(result)

#<=等价=>

result = map(lambda x: x**2, range(5))
print(list(result))


# eg.3
result = map(None,[1,2,3],[5,6,7])

print(result)

result = zip([1,2,3],[5,6,7])
print(list(result))