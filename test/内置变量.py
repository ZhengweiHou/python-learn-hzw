def func1():
    print(dir())






if __name__ == "__main__":
    for key in dir():
        exec('print("{}=%r"%{})'.format(key,key))