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


from collections import Counter

