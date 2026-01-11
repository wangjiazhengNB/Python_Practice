s = [91, 2, 3, 85, -43, 61]

#正向和反向索引
# print(type(s))
# print(s[0])
# print(s[-6])

# #修改
# s[0] = "DEF"
# print(s)

# #删除
# del s[0]
# print(s)

#切片操作
# print(s[0:5:1])
# #也可以进行省略因为初始下标0和步长1都是默认的
# print(s[:5])

print(s)
s.append(110)
print(s)
s.insert(0, 110)
print(s)
#移除第一个指定位置的元素
s.remove(110)
print(s)
#若无指定索引，默认pop删最后一个
s.pop(0)
print(s)
s.sort()
print(s)
s.reverse()
print(s)


