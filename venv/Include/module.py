"""
This part is about learn module
import module must use the keyword "import"
导入模块时考虑顺序为系统自带模块，引用别人创建的模块，自己创建的模块
"""

"""
1、导入模块的方式
"""
import math

print("50's sqrt is: %.6f" % math.sqrt(50))
"""
有时候只需要用到模块中的某个函数，只需要引用该函数即可
from 模块名 import 函数名1，函数名2...
这种调用方式引入时调用函数只给出函数名，但是当两个模块中含有
相同的函数名时，后面一次的引用会覆盖前面一次的引用
"""
from math import sqrt, pow

print("%.6f  %.2f" % (sqrt(50), pow(5, 2)))

"""
2、列举模块中的内容
dir(模块名)返回一个排好序的字符串列表
"""
content = dir(math)
print(content)

"""
定义自己的模块
在python中，每个python文件都可以作为一个模块，模块的名字就是文件的名字
"""
import module_import
module_import.fib(5)
