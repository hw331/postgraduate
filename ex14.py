#import moudles argv from sys
from sys import argv
#解包 argv 分为两段 有 script 以及你输入的文件名
script , filename = argv
#定义并打开文件filename
txt = open(filename)
#输出字符串“你的文件名”
print ("Here is your file %r:"%filename)
#打印出filename 所有内容
print (txt.read())
txt.close()
#打印字符串
print ("Type the filename again:")
#定义变量将输入的参数传递给他
file_again =input(">")
#打开文件
txt_again = open (file_again)
#打印所有文本
print (txt_again.read())
txt_again.close()

