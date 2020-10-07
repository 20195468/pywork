print("这里是元组的学习")
"""
Python的元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号，列表使用方括号。

元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

元祖中可以有不同类型的元素
"""
name_first_tuple = ("shabby", 13, ["zhangSan", "liSi", "wangWu"])
"""
创建空元素元组
"""
name_second_tuple = ()

"""
创建单个元素的元组，元素后必须加,
"""
name_third_tuple = ("赵四",)
print(type(name_third_tuple))  # tuple类型
# name_third_tuple=("赵四")
# print(type(name_third_tuple)) # String类型

"""
访问元组
"""
print(name_first_tuple[0])
print(name_first_tuple[0:3])
print(name_first_tuple[0:len(name_first_tuple)])

"""
元组中元素不可修改，但是两个元组可以连接
"""
name_fourth_tuple = name_first_tuple + name_third_tuple
print(name_fourth_tuple)

"""
元组的索引，截取
"""
print("元组中的倒数第二个元素为", end=":")
print(name_first_tuple[-2])  # 表示倒数第二个元素
print("截取下标以后(包含该下标)的元素", end=":")
print(name_fourth_tuple[1:])  # 截取下标以后(包含该下标)的元素

"""
元组中的内置函数
"""
# 元组的长度
print("元组中的长度为%d" % len(name_fourth_tuple))
# 元组中的最大值,元组中只能比较相同类型
# 若有不同类型就报错
number_tuple = (1, 2, 3, 4, 5)
print("元组中的最大值为%d" % max(number_tuple))
# 元组中的最小值
print("元组中的最小值为%d" % (min(number_tuple)))

# 元组,字符串和列表之间可以相互转换
list_1=list(number_tuple)
print(list_1)
list_1.insert(2,8)
print(list_1)
tuple_list=tuple(list_1)
print("__________")
print(tuple_list)
str_tuple=str(tuple_list)
print("_________")
print(str_tuple)
print(str_tuple[2])