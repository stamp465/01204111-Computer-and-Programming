n = int(input())
arr = [ [' ']*n for i in range(n) ]
for i in range(n) :
	for j in range(n) :
		if i==j or i+j==n-1 :
			print('.',end='')
		elif i==0 or j==0 or i==n-1 or j==n-1:
			print('.',end='')
		else :
			print(' ',end='')
	print()
