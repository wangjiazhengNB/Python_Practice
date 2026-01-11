#字符串 不可变的 -- 不能将s[i] = "s"这是错的

s = "   Hello-Python-C++-java   "

#切片
#步长若取负数则是重后往前截取
print(s[0:10:2])

#得到第一次出现的索引位置
index = s.find("-")
print(index)

c = s.count("o")
print(c)

smax = s.upper()
print(smax)
smin = s.lower()
print(smin)

#splict()将字符串案指定字符串切割-列表
ss = s.split("-")
print(ss)

#strip()去除字符串两边空格
ss = s.strip()
print(ss)

sr = s.replace("-", "_")
print(sr)