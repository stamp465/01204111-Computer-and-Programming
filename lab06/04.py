def print_matrix(A) :
	x = len(A)
	y = len(A[0])
	for i in range(0,x) :
		for j in range(0,y) :
			print(f'{A[i][j]:^6}', end = ' ')
		print()

def transpose_matrix(A) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*x for i in range(y) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[j][i] = A[i][j]
	return ans

A = [[1,2],[3,4],[5,6]]
ans = transpose_matrix(A)
print_matrix(ans)