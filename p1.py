import sys


class Test:
    pass


t1 = Test()
t2 = Test()
t3 = Test()
print(sys.getrefcount(t1))
print(sys.getrefcount(t2))
print(sys.getrefcount(t3))
