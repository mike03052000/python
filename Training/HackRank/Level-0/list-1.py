import os

def list_intersect():
    pass
aList = [123, 'xyz', 'zara', 'abc', 'jobh',123,'abc',235]
print("Reverse List : ", aList[::-1])
print("Original List : ", aList)

a1=[8,90]
print("%r extend %r " % (aList , a1))
aList.extend(a1)
print("result = %r" % (aList))
print("%s, index = %d" %('abc' , aList.index('abc')))
print("%s, index = %d" %('abc', aList.index('abc',0,5)))
print("%s, index = %d" %('abc', aList.index('abc',5)))
aList.reverse();
print("Reverse List : ", aList)
print("Original List already change: ", aList)
print("count =", aList.count(123),aList.count('xyz'))

try:
    print("index = ", aList.index('abc',3,5))
except ValueError as msg:
    print(msg)
    # raise
except:
    print("index = ", aList.index ('123'))
else:
    print ("123 index = ", aList.index (123, 0, 5))
finally:
    print("Finally")

aList.remove(123)
print("remove = ", aList)

aList.remove("xyz")
print("remove = ", aList)

aList.clear()
print("clear = ", aList)

c="hh"
aList.append(c)
print("append List : ", aList)

aList.insert(0,"h")
print("Insert List : ", aList)

c=aList.pop(0)
print("pop List ", aList, " item ",c)

