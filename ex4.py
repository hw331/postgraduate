#定义变量car并赋值100
cars=100
#定义变量car空间并赋值浮点数4.0
space_in_cars=4.0
#定义驾驶员数量30
drivers=30
#定义游客数90
passengers=90
#定义cars_not_driven并传参进行计算
cars_not_driven=cars-drivers
#定义cars_driven并传参进行计算
cars_driven=drivers
#定义运输能力变量并进行计算
carpool_capacity=cars_driven*space_in_cars
#定义平均值变量并传参进行计算
average_passengers_per_car=passengers/cars_driven

#输出字符串并传输参数cars
print ("There are",cars,"cars available.")
#输出字符串并传输参数drivers
print ("There are only ",drivers,"drivers available.")
#输出字符串并传输参数cars_not_driven
print ("There will be ",cars_not_driven,"empty cars today.")
#输出字符串并传输参数carpool_capacity
print ("We can transport",carpool_capacity,"people today.")
#输出字符串并传输参数passengers
print ("We have ",passengers,"to carpool today.")
#输出字符串并传输参数average_passengers_per_car
print ("We need to put about",average_passengers_per_car,"in each car.")