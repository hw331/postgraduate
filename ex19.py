#导入文件
from sys import argv
#拆包
script ,input_file = argv
#定义函数print_all 读取文件并打印
def print_all(f):
	print (f.read())


#定义函数，用于定位文本中的首位	
def rewind(f):
	f.seek(0)
	
#定义输出文本函数，输出line_count,以及输入文件f的readline函数执行结果
def print_a_line(line_count,f):
	print (line_count,f.readline())
	
current_file = open(input_file)

print ("first let's print the whole file :\n")

print_all(current_file)

print ("Now let's rewind ,kind of like a tape.")

rewind(current_file)

print ("Let's print three lines:")

current_line=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

current_file.close()