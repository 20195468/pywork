import random

print("欢迎进入到py的学习，在这里你会感受到py语法的神奇和魅力")

"""
下面是py运算符的学习
py不需要加分号
在py中取整除用//和java中的除法不同
"""

# 输出多个转行字符串
print("""
你好，这是第一行
这是第二行
""")
# 转义字符运用\或者r''
print(r'\n')

print(9 / 2)  # 结果为4.5
print(9 // 2)  # 结果为4
# 幂运算符号也不相同**表示幂运算  java中math.pow表示幂运算
print(2 ** 3)  # 结果为8
# print()不换行输出
print("不换行输出", end="")
# *也可以表示字符串的数量
print("\n" + "你好" * 3)  # 结果为 你好你好你好

# py不需要声明变量
a = 1
b = 2
"""
print()输出格式为1、字符串+字符串：str+str
                 2、字符串, 变量：str,变量（,会自动添加一个空格）
"""
print("a=", a)

"""
当对一个变量赋值时会自动区分该变量的类型
type()函数输出变量类型类型
input()获得从键盘输出的值相当于c中的scanf()
input()将所有的输入值转换为String类型而不是对应的int或者float类型
"""
print(type(a))
name_str = input("请输入一个字符串：")
print("该字符串为：" + name_str)

"""
float()可将输入的数字转化为float类型
int()可将输入的数字转化为int()类型
"""
a = input("请输入一个整数：")
print("强制转换为int类型：", int(a))
print("强制转换为float类型：", float(a))

"""
print()的格式化输出
%06d 输出六位整数（不足六位用0补齐,多于六位的显示原数字）
%.02 输出两位小数
%s 输出字符串/
"""
a = input("请输入一个整数：")
print("变量格式化输出%06d %.03f" % (int(a), 9.8))
# print("变量格式化输出%.03f" % float(a))

"""
if判断语句用法
"""
age = 3
if age >= 18:
    print("你已经成年")
elif age < 18 and age > 6:
    print("你是青少年")
else:
    print("你是少年")

"""
while用法
"""
a = 1
while a <= 5:
    print(a, end=" ")
    a += 1

"""
for循环的三种循环方式
"""
for letter in "python":
    print("字母是：", letter)

fruits = ["apple", "banana", "panel"]
for index in range(len(fruits)):
    print(fruits[index])

for fruit in fruits:
    print(fruit)

"""
函数创建，函数只能放在调用者的前方和java不同
"""


def sum(num1, num2):
    return num1 + num2


print(sum(7, 8))

# 导入模块，调用随机数
random.randint(3, 5)
