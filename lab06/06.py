#06
def print_matrix(A) :
	x = len(A)
	y = len(A[0])
	for i in range(0,x) :
		for j in range(0,y) :
			print(f'{A[i][j]:^6}', end = ' ')
		print()

def power_matrix(A,c) :
	ans = A 
	#print(A)
	for i in range(1,c) :
		ans = mul_matrix(A,ans)
	return ans		

def mul_matrix(A,B) :
	x1 = len(A)
	x2 = len(A[0])
	y1 = len(B)
	y2 = len(B[0])
	ans = [ [0]*y2 for i in range(x1) ]
	for i in range(0,x1) :
		for j in range(0,y2) :
				for l in range(0,y1) :
					ans[i][j] += A[i][l]*B[l][j]
	return ans

A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2
ans = power_matrix(A,c)
print_matrix(ans)