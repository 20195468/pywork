"""
python文件的使用
"""
"""
文件的覆盖和追加
覆盖"w"
追加"a"
"""
helloFile=open("hello.txt","w")
helloFile.write("firsr line")
helloFile.write("\n")
helloFile.write("second line")
helloFile.close()
