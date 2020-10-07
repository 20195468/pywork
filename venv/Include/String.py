print("这里是字符串的学习")
# 字符和数字之间的转化
print(ord('A'))  # 65
print(chr(65))  # A

"""
b'ABC'为bytes类型表示
"""
x = b'ABC'
print(x)
y = 'ABC'
print(y)

"""
如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
要把bytes变为str，就需要用decode()方法：
"""
# print(b'ABC'.decode('ascii'))
"""
以Unicode表示的str通过encode()方法可以编码为指定的bytes
"""
print('ABC'.encode('ascii'))
