dict1 = {"欧文": 11, "乔丹": 23, "科比": 24, "詹姆斯": 23}


print(dict1);

#添加
dict1["罗斯"] = 1;

print(dict1["罗斯"])

#查询(2种方法)
print(dict1["罗斯"]);
print(dict1.get("罗斯"))

#删除
number = dict1.pop("罗斯")
del dict1["乔丹"]
print(dict1)

#获得所有的key,
#获得所有的value
#获得所有的键值对
print(dict1.keys())
print(dict1.values())
print(dict1.items())

#遍历(3种)
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]} : {item[1]}")

for k, v in dict1.items():
    print(f"{k} : {v}")
    