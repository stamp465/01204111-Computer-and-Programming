n = int(input("input: "))
for i in range(0,n//2+1) :
	for j in range(0,n-i) :
		print(" ",end='')
	for j in range(0,i*2+1) :
		print("#",end='')
	print("")
for i in range(n//2-1,-1,-1) :
	for j in range(0,n-i) :
		print(" ",end='')
	for j in range(0,i*2+1) :
		print("#",end='')
	if i!=0 :
		print("")