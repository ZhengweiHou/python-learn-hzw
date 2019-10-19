from enum import Enum, unique

@unique
class IdType(Enum):
    I = ("身份证 ", "01")
    A = ("军官证", "07")
    I2 = ("身份证 ", "01")

# ====使用枚举====
print(IdType.I, IdType.I.name, IdType.I.value)  # IdType.I I 01

# ====遍历枚举====
for item in IdType:
    print(item.name, item.value)
# I ('身份证 ', '01')
# A ('军官证', '07')

for name, member in IdType.__members__.items():
    print(name, member.value[0], member.value[1])
# I 身份证  01
# A 军官证 07

# ====枚举转换====
#通过value转换成枚举
print(IdType(("身份证 ", "01")))   #IdType.I

# print(IdType.)






