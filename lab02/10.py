import datetime 
d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))
a = datetime.datetime(y, m, d) 
b = datetime.datetime(y, 1, 1) 
c = a-b
print(c.days+1)