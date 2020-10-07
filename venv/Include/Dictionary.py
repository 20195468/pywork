print("这里是字典的学习")
"""
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：

字典类似于java中的map集合

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

一个简单的字典实例：
"""
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}

"""
访问字典里的值

把相应的键放入到方括号中(方括号中只能填入相应的键值)，如下实例:
"""
print(dict1['abc'])

"""
修改字典(直接将修改的值进行赋值)

添加字典中的元素(将需要添加的键值直接赋值)
eg : dict[key] = value
"""
dict['Name'] = 'XiaoZe'
print(dict['Name'])
dict['code'] = 99
print(dict)

"""
删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令
"""
print("原字典中的元素：", dict2)
del dict2[98.6]
print("删除字典中的一个元素：", dict2)
dict2.clear()
print("清空字典中的元素：", dict2)
# # 在这里会报错，因为该字典已经不存在
# del dict2
# print("删除字典：", dict2)

"""
字典中的复制和赋值
字典中的复制(copy)指单纯的将数据进行复制
而赋值是指将地址值赋值给另一个对象(和c中的指针赋值比较相似)
"""
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)
# 输出结果
print(dict1)  # {'user': 'root', 'num': [2, 3]}
print(dict2)  # {'user': 'root', 'num': [2, 3]}
print(dict3)  # {'user': 'runoob', 'num': [2, 3]}

"""
Python 字典 fromkeys() 函数用于创建一个新字典，
以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
"""
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict))  # {'name': None, 'age': None, 'sex': None}
dict = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict))  # {'name': 10, 'age': 10, 'sex': 10}

"""
Python 字典 get() 函数返回指定键的值，如果键不在字典中返回默认值。
"""
dict = {'Name': 'Runoob', 'Age': 27}
print("Age 值为 : %s" % dict.get('Age'))
print("Sex 值为 : %s" % dict.get('Sex', "NA"))

"""
Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。

而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
"""
# 检测键 Age 是否存在
if 'Age' in dict:
    print("键 Age 存在")
else:
    print("键 Age 不存在")
# 检测键 Sex 是否存在
if 'Sex' in dict:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")

# not in
# 检测键 Age 是否存在
if 'Age' not in dict:
    print("键 Age 不存在")
else:
    print("键 Age 存在")

"""
Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
"""
dict = {'Name': 'Runoob', 'Age': 7}
print("Value : %s" % dict.items())  # Value : dict_items([('Name', 'Runoob'), ('Age', 7)])
