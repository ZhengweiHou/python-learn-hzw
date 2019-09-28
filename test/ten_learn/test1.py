import re

a = 'C|C++|Java|C#|Pyton|1|2|hzw|3'

r = re.findall('\d',a)
print(r)
