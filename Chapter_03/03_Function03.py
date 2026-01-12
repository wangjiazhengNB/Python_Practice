#不定长参数
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data)

# print(calc_data(2, 4, 6, 66, 24, 28))

#传参为函数的例子
# def add(x, y):
#     return x + y

# def calc(x, y, oper):
#     return oper(x, y)

# print(calc(10, 20, add))

#匿名函数
# out_line = lambda : print("------------")
# out_line()

# add = lambda x, y : x + y
# print(add(10, 20))

#因为默认是list是按每个元素字母序排序
#我现在想按长度排序

data_list = ["C++", "C", "Python", "Java", "PHP", "JavaScript", "Rust"]
print(data_list)

data_list.sort()
print(data_list)
#从小到大排序
data_list.sort(key=lambda item : len(item))
print(data_list)

#从大到小排序
data_list.sort(key=lambda item : len(item), reverse=True)
print(data_list)


#类型注释
a2: int = 110
score2: float = 110.1
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A", "B", 1, 2]
phones2: set[str] = {"123", "456", "789"}
options2: dict[str, int] = {"count": 1, "total": 2}
goods2: tuple[str, int, int] = ("手机", 110, 1)


#函数类型注解

def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(8.5)
print(al)
