 # 输出hello world

print("Hello World")
print("Hello Python")
print("----------------")

# true false 为合法标识符
# True False 为非法标识符

# type()语句，来得到数据的类型
print(type("hello"))
print(type(10))
print(type(10.5))
print(type(True))
print(type(None))


# 字符串的三种定义方式
s1 = "hello"
s2 = 'hello'
s3 = """
hello :
    大家好
    欢迎大家来到Python的语法学习
"""
print(s1)
print(s2)
print(s3)

#转义符号\
s = 'hell\'o'
print(s)

#字符串拼接
t1 = "人生苦短" "及时行乐" ","
t2 = "人生精彩" "创造非凡" "。"
t3 = t1 + t2
print(t3)

#字符串格式化, 单个，多个，方式1
s1 = "正哥"
s2 = "最帅"
print("大家好, 我是%s, 欢迎大家" % s1)
print("%s%s" % (s1, s2))

#方式2
print(f"大家好我是 {s1} ")

#输入 输出
# name = input("请输入你的名字: ")
# age = input("请输入你的年龄: ")
# print(f"你的姓名是{name}, 年龄为{age}岁")

#算术运算符
# + 加
# - 减
# * 乘
# / 除 这个得到的结果为float类型
# // 整除
# % 取模
# ** 幂

print("汪嘉正","最帅")
x = 10
y = 20
print("x + y = ", x + y)

#比较运算符与C++一样

#逻辑运算符
# and 并且
# or 或者
# not 非

n = int(input("请输入一个整数: "))
#链式结构
print(f"{n}在10 ~ 20之间: ", 10 <= n <= 20)
