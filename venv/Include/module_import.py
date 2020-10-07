"""
该文件作为一个模板供module调用
"""


# 返回前n项斐波那契数列
def fib(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(b)
        num = a + b
        a = b
        b = num
    print(result)
    return result


"""
这种方式只会对该模块进行测试而不是在其他模块导入该模块时
也执行测试语句
"""
# 测试模块
if __name__ == "__main__":
    fib(6)
