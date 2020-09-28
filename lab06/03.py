def print_matrix(A) :
	x = len(A)
	y = len(A[0])
	for i in range(0,x) :
		for j in range(0,y) :
			print(f'{A[i][j]:^6}', end = ' ')
		print()

def mul_const(A,c) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*y for i in range(x) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[i][j] = A[i][j] * c
	return ans

A = [[1,2],[3,4],[5,6]]
c = 2
ans = mul_const(A,c) 
print_matrix(ans) 