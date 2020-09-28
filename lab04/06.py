n = int(input("Input: "))
b = n + 10
a = [[0] * b for i in range(b) ] 
a[0][0] = 1
for i in range(1,n+1) :
	for j in range(1,i+1) :
		a[i][j] = a[i-1][j-1] + a[i-1][j]
		print(a[i][j],end=' ')
	print()