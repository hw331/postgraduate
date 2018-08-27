#定变量x
x = "There are %d typesof people." % 10
#定义字符串
binary = "binary"
#定义字符串
do_not = "don't"
#定义参数并传参
y = "Those who know %s and those who %s."%(binary,do_not)

#输出x
print (x)
#输出y
print (y)
#输出字符串
print ("I said: %r."%x)
输出字符串
print ("I also said: '%s'."%y)
#定义变量
hilarious =False
#定义变量
joke_evaluation = "Isn't that joke so funny?! %r "
#输出字符串？？？  %这样为啥
print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side ."
print (w+e)