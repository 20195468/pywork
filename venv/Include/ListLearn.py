"""
列表的使用，创建列表使用[]
"""
print("这里是python中的list学习")
name_list = ["Zhangsan", "Lisi", "Wangwu"]
name_list.append("Zhaoliu")
# 打印列表中的所有内容
print(name_list)
# 在指定位置添加数据
name_list.insert(1, "XiaoMing")
print("在指定位置添加数据:", name_list)
# 将列表二添加到列表一
name_list2 = ["XiaoYing"]
name_list.extend("将两个列表和二为一", name_list2)
print(name_list)
# 列表内容的删除
del name_list[1]
print(name_list)
# 删除第一个出现的指定内容
name_list.remove("XiaoYing")
print(name_list)
# 删除末尾数据 ()内添加内容为指定下标数据
name_list.pop()
print(name_list)
# 统计列表长度
print(len(name_list))
# 统计指定数据出现的次数
name_list.append("Wangwu")
print(name_list)
print(name_list.count("Wangwu"))
# 升序排序
number_list = [1, 4, 3]
number_list.sort()
print(number_list)
# 降序排列
number_list.sort(reverse=True)
print(number_list)
# 反转
number_list.reverse()
print(number_list)
name_list.sort()
print(name_list)

print("通过 i for row in range(argu)形式创建链表")
cols = 6
rows = 3
matrix = [[0 for col in range(cols)] for row in range(rows)]
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
        if (j == cols - 1):
            print()
list = [1 for row in range(rows)]
for i in range(rows):
    print(list[i], end=" ")
