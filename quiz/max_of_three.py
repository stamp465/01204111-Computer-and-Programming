import math
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))
maxx = max(a,b,c)
if math.floor(maxx) == maxx :
	maxx = math.floor(maxx)
print(f"Maximun is {maxx}")