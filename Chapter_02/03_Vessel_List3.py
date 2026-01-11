#生成1-20的平方列表 --》 range(1, 21)

#方法1
num_list = []
for i in range(1, 21):
    num_list.append(i**2)


print(num_list)


#列表推导式
#方法2
#语法格式1：[要插入的值 for i in 序列/列表]
#语法格式2：[要插入的值 for i in 序列/列表 if 条件]
num_list2 = [i**2 for i in range(1, 21)]
print(num_list2)


num_list2 = [i**2 for i in range(10, 1000) if i & 1 == 0]
print(num_list2)