import re

#小写字母转大写 re.sub()
str = 'The Zen of Python, by Tim Peters'

def upper(value):
    matched = value.group()
    if ord(matched) <= 122 and ord(matched) >= 97:
        return chr(ord(matched) - 32)
    else:
        return matched

result = re.sub('[a-z]',upper,str,0)

print(result)

r = re.search('The',str)
print(r)






