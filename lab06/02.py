def print_matrix(A) :
	x = len(A)
	y = len(A[0])
	for i in range(0,x) :
		for j in range(0,y) :
			print(f'{A[i][j]:^6}', end = ' ')
		print()

def minus_matrix(A,B) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*y for i in range(x) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[i][j] = A[i][j] - B[i][j]
	return ans

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
ans = minus_matrix(A,B)
print_matrix(ans)