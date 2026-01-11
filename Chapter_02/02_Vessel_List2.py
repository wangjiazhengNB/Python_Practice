#将用户5个数存入列表，
#并求最大值，最小值，平均值


# num_list = []

# for i in range(5):
#     num = int(input("请输入有效数字："))
#     num_list.append(num)

# print("数字列表 ", num_list)


# #sum()是求和
# #len()是获取元素的个数（列表的长度）
# num_list.sort()
# print(num_list)
# print("max: ", num_list[0])
# print("最小值：", num_list[-1])
# print("平均值：", sum(num_list) / len(num_list))

#合并列表
list1 = [1, 24, 124, 1123, 98]
list2 = [32, 243, 23, 98, 13]

#复杂的合并方法
for num in list2:
    list1.append(num)

print(list1)

#简化的合并方法
#运用*解包和组包技巧技巧
#解包将容器解开成一个个独立的元素
#组包将多个组合并到一个容器
new_list = [*list1, *list2]
print(new_list)

#第三个方法最简化
new_list = list1 + list2
print(new_list)



#去重
list3 = []
for num in list1:
    if num not in list3: # 存在返回True， 不存在返回False
        list3.append(num)
print("去重之后的结果：", list3)