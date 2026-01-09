#while循环

# i = 0
# while i < 5:
#     print("我是大帅哥")
#     i += 1

#计算1 ~ 100 之间偶数的累加之和
# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         total += i
#     i += 1
# print(total)

#for循环

# msg = input("请输入要遍历的字符串: ")
# for s in msg:
#     print(f"元素: {s}")
# else:
#     print("遍历结束")

#range函数
#range(end) 获得0 ~ end - 1 之间的数据集
#range(start, end) 获得start ~ end - 1 之间的数据集
#range(start, end, step)
# 获得start ~ end之间间隔step的数，不包含step

#案例1 获得1 - 100 间的奇数和
# total = 0
# for i in range(1, 101):
#     if i % 2 == 1:
#         total += i

# print(total)

# m = int(input("请输入长方形的长度："))
# n = int(input("请输入长方形的宽度："))

#end=""每一次输出结尾就输出一个""
# for i in range(n):
#     for j in range(m):
#         print("*", end=" ")
#     print()

#输出99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}", end = "\t")
    print()

