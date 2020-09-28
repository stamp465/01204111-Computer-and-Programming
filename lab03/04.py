import math
def fac(n) :
	fact = 1
	for i in range(1,n+1): 
		fact = fact * i 
	return fact

degree = float(input("degree: "))
de = degree
degree *= math.pi/180
sin = float(0)
cos = float(0)
for n in range(1,11) :
	sin += ((-1)**(n-1))*(degree**(2*n-1))/fac(2*n-1)
	#print(sin)
print("sin(%.2f): %.10f"%(de,sin))
for n in range(0,11) :
	cos += ((-1)**n)*(degree**(2*n))/fac(2*n)
	#print(cos)
print("cos(%.2f): %.10f"%(de,cos))