# 正则表达式
## re模块
### re函数
1. **`findall()`**
    返回匹配的字符
1. **`sub()`**
    替换匹配的字符

1. **`match()`**
    从目标字符^处匹配字符，返回match对象
    
1. **`search()`**
    返回匹配的match对象

1. **`group()`**
    通过match对象获取对应组，默认返回全部匹配，参数指定返回组号
    
### e.g.
#### 小写字母转大写 re.sub()
``` python
import re

str = 'The Zen of Python, by Tim Peters'

def upper(value):
    matched = value.group()
    if ord(matched) <= 122 and ord(matched) >= 97:
        return chr(ord(matched) - 32)
    else:
        return matched

result = re.sub('[a-z]',upper,str,0)

print(result)       # THE ZEN OF PYTHON, BY TIM PETERS
```

# JSON
## json模块
`import json`

### 反序列化
`json.loads(json_str)`

### 序列化
`json.dumps(obj_dict)`

### e.g.
``` python
class Student:
    def __init__(self,name=None,age=0):
        self.name = name
        self.age = age

import json
student_json = '{"name":"张三","age":15}'


# 反序列化
student = json.loads(student_json)
print(type(student),student)            # <class 'dict'> {'name': '张三', 'age': 15}

student = Student(**student)
print(type(student),student.__dict__)   # <class '__main__.Student'> {'name': '张三', 'age': 15}


# 序列化
student_json = json.dumps(student.__dict__,ensure_ascii=False)  # ensure_ascii
print(type(student_json),student_json)  # <class 'str'> {"name": "张三", "age": 15}
```
