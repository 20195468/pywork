print("这里是python集合的学习")
"""
总结：创建列表使用[],创建字典使用{}(要有键：值),创建集合用{}和set()

集合（set）是一个无序的不重复元素序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

该集合和java中的set用法相似
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("集合具有去重功能")
print(basket)  # {'banana', 'apple', 'orange', 'pear'}

"""
判断某元素是否在集合中存在用 in 关键字
"""
if "orange" in basket:
    print(r'"orange"在集合中')
else:
    print(r'"orange"不在集合中')

"""
set方式创建集合
"""
a = set('abracadabra')
b = set(("alacazam", "nihao"))
print(a)  # {'c', 'a', 'r', 'b', 'd'}
print(b)  # {'nihao', 'alacazam'}
"""
两集合间的运算
"""
# 集合a中包含而集合b中不包含的元素(类似离散数学)
print(a - b)  # {'d', 'b', 'r'}
# 集合a或b中包含的所有元素(表示析取)
print(a | b)  # {'d', 'l', 'r', 'a', 'z', 'c', 'm', 'b'}
# 集合a和b中都包含了的元素(表示合取)
print(a & b)  # {'c', 'a'}
# 不同时包含于a和b的元素
print(a ^ b)  # {'r', 'l', 'z', 'm', 'd', 'b'}

"""
添加元素
"""