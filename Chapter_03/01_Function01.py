#基础的定义和c语言很像

# def out_line():
#     print("I am goat!!!")
#     print("I am Jordon")

# out_line()

# def circle_area(r):
#     area = 3.14 * r ** 2
#     return area

# print(circle_area(10))


#函数的说明文档
def rectangle_area(l, w):
    """
    rectangle_area 的 Docstring
    :param l: 长度
    :param w: 宽度
    :return 长方形的面积
    """
    area = l * w
    return area


help(rectangle_area)