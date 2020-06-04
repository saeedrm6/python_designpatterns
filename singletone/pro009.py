from pro008 import SingletonObject

obj1 = SingletonObject()
obj1.val = "Obj value 1"
print("print obj1: ",obj1)

obj2 = SingletonObject()
obj2.val = "Obj value 2"
print("print obj1: ",obj1)
print("print obj2: ",obj2)

print(obj1.val)
print(obj2.val)

# print obj1:  <pro008.SingletonObject.__SingletoneObject object at 0x7f50d3da2908> Obj value 1
# print obj1:  <pro008.SingletonObject.__SingletoneObject object at 0x7f50d3da2908> Obj value 2
# print obj2:  <pro008.SingletonObject.__SingletoneObject object at 0x7f50d3da2908> Obj value 2
# Obj value 2
# Obj value 2
