#set的定义

#直接这样a = {}这是字典

a = {1, 2, 3}
b = set();

print(type(b))

t = {1, 2, 3}
print(t)

t.add(4)
print(t)

t.remove(1)
print(t)

tt = t.pop()
print(t)
print(tt)

t.clear()
print(t)

t1 = {1, 2, 3}
t2 = {2, 3, 4}
#求两个集合的差集
print(t1.difference(t2))
print(t2.difference(t1))
#求两个集合的并集和交集
print(t1.union(t2))
print(t1.intersection(t2))
