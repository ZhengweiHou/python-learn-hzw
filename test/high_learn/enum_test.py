from enum import Enum

class IdType(Enum):
    I = ("身份证 ", "01")
    T = ("临时身份证 ", "x1")
    A = ("军官证", "07")

print(IdType.I, IdType.I.name, IdType.I.value)  # IdType.I I 01

for item in IdType:
    print(item.name,item.value)

for name,member in IdType.__members__.items():
    print(name, member.value[0], member.value[1])


