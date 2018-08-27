from sys import argv

script,filename = argv

print ("We are going to erase %r."%filename)
print ("If you don't want that ,hit CTRL-C(^c).")
print ("If you want that ,hit RETURN.")

input("?")

print ("Opening file ...")
# 'w'???
target = open (filename,'w')

print ("Turncating the file.Goodbye!")
#delete 
target.truncate()

print ("Now I'm going to ask you three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print ("I'm going to write these to the file.")

#可以使用变量a来代替'\n'也就不用每次输入
#target.write(line1+'\n'+line2+'\n'+line3)
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print ("And finally,we close it.")
target.close()