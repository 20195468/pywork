# python中函数不能向前引用
def add(a, b):
    return a + b


print(add("a", "b"))
"""
Lambda表达式
"""
f = lambda x, y, z: x + y + z
print(f(1, 2, 3, ))
m = [(lambda x: x ** x), (lambda y: y // 9), (lambda x: x / 9)]
print(m[0](1), m[1](18), m[2](18))
"""
在某些情况下可以通过特殊的当时在函数内部修改实参的值
"""


def modify1(m1, k):
    m1 = 2
    k = [4, 5, 6]


def modify2(m1, k):
    m1 = 2
    k[0] = 0


n = 100
m = [1, 2, 3]
print("在函数内部对实参的修改")
print("原函数为：")
print(n, " ", m)
print("函数一的调用")
modify1(n, m)
print(n, " ", m)
print("函数二的调用")
modify2(n, m)
print(n, " ", m)

"""
函数在声明时可以指定参数值
"""


def display(a="河南", b="真好"):
    print(a + b)


display()
display(a="大河南")
display(b="骄傲")
display("河南人")
print("只与参数位置有关，而与参数的赋值无关")
display(b="真好", a="河南")
"""
函数中可以定义任意个参数 使用*或**
*表示将没有匹配的值放在同一个元组中
**表示将没有匹配的值都放在一个字典中
"""


def storename(name, *nickName):
    print("real name is %s" % name)
    for nickname in nickName:
        print("little name is", nickname)


def demo(**p):
    for item in p.items():
        print(item)


storename("张海")
storename("张海", "小海")
storename("张海", "小海", "小豆豆")

demo(a=1, b=2, c="3")

"""
变量的作用域
"""
globalnum = 1


def fun():
    global globalnum
    globalnum = globalnum + 1;
    print(globalnum)
    nonnum = 3

    def innerfun():
        nonlocal nonnum
        nonnum = nonnum + 2
        print(nonnum)

        global globalnum
        globalnum = globalnum + 1;
        print(globalnum)

    innerfun()


fun()

"""
闭包和函数的递归调用
"""

def func_lib():
    def add(x, y):
        return x + y

    return add


fadd = func_lib()
print(fadd(3, 5))

x = -9.8
x = abs(x)
print(x)
x = complex(9, 3)
print(x)  # 形式为(9+3j)
x, y = divmod(9, 3)
print(x, " ", y)
x = "string"
x = 'a'
