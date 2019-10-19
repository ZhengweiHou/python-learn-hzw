#e.g.1
result = filter(lambda x:x%2,range(10))
print(list(result)) # [1, 3, 5, 7, 9]



# e.g.2
import re
result = filter(lambda x: re.search('[A-Z]',x),'AbCdaBcD')
print(list(result)) # ['A', 'C', 'B', 'D']



