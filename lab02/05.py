fibo = int(input("Day: "))
lis = []
for i in range(fibo) :
	if(i<2) : lis.append(1)
	else :
		lis.append(lis[i-1]+lis[i-2])
print(*lis) 