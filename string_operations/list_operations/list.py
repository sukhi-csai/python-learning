a = [1,2,3]
a.append(4)
print("After append:", a)
b = [1,2,3]
b.clear()
print("After clear:", b)
c =[1,2,3]
c.extend([4,5])
print("After extend:", c)
d =[10,20,30,40,50]
print("Popped value:", d.pop())
print("After pop:", d)
f =[5,10,15,20]
print("Index of 10:", f.index(10))
g = [1,2,3,4,5]
g.insert(2,3)
print("After insert:", g)
h = [1,2,3,4]
h.reverse()
print("After reverse:", h)
i = [3,1,2,4]
i.sort()
print("After sort:", i)
j = [1,2,3]
k = j.copy()
k.append(4)
print("Original list j:", j)
print("Copied list k:", k)
