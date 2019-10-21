# === 1 ===
print('' == None)       # False
print([] == None)       # False
print(0 == None)        # False
print(False == None)    # False
print(type(None))       # <class 'NoneType'>


# === 2 ===
a = []

if not a:
    print('S')
else:
    print('F')
# S

if a is None:
    print('S')
else:
    print('F')
# F

