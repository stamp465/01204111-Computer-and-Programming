a = int(input("N: "))
c = 0
lis = []
while True:
	check = 0
	check2 = 0
	b = a+2
	for i in range(2,a) :
		if a%i ==0 :
			check = 1
	for i in range(2,b) :
		if b%i ==0 :
			check2 = 1
	if check == 0 and check2 == 0 :
		lis.append(a)
		lis.append(b)
		break
	a += 1
print("(%d, %d)"%(lis[0],lis[1]))