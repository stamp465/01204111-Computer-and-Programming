R = int(input("R: "))
C = int(input("C: "))
sum = int(0)
while R>0 and C>0:
	sum += R*C
	R -= 1
	C -= 1
print(sum)