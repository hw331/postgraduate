def add(a,b):
	print("Adding %d + %d"%(a,b))
	return a+b
	
def subtract(a,b):
	print ("subtract %d-%d"%(a,b))
	return a-b
	
def multiply(a,b):
	print("multiply %d*%d"%(a,b))
	return a*b
	
def divide(a,b):
	print ("divide %d / %d"%(a,b))
	return a/b
	
print ("Let's do some math with just functions")

floor=add(4,1)

room=subtract(516,2)

age=multiply(11,2)

number=divide(8,2)

print("We are at the %d ,and the room %d, I'm %d years old,finally, there are %d people in the room  \n"%(floor,room,age,number))

final = add(floor,multiply(divide(room,age),number))

print ("we need to put %d on the window",final,"ok")
