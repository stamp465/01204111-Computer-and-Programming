def printt(x,y,arr) :
	for i in range(1,x) :
		for j in range(1,y) :
			print(arr[i][j],end=' ')
		print()

def setmatrix(m,n) :
	return [ [0]*(m+2) for i in range(n+2) ]

def setmind(x,y,arr) :
	for i in range(-1,2,1) :
		for j in range(-1,2,1) :
			#print("%d %d"%(x+i,j+y))
			if arr[x+i][y+j] != 'X' :
				arr[x+i][y+j] += 1
	arr[x][y] = 'X'
	'''for i in range(1,5) :
		print(arr[i])'''
	return arr

size = input("Grid Size: ").split()
arr = setmatrix(int(size[1]),int(size[0]))
num = int(input("Number of mine(s): "))
for i in range(num) :
	mind = input("Mine#%d: "%(i+1)).split()
	setmind( int(mind[1])+1,int(mind[0])+1,arr)
printt(int(size[1])+1,int(size[0])+1,arr)