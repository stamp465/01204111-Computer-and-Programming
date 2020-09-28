def print_matrix(A) :
	x = len(A)
	y = len(A[0])
	for i in range(0,x) :
		for j in range(0,y) :
			print(f'{A[i][j]:^6}', end = ' ')
		print()

def plus_matrix(A,B) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*y for i in range(x) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[i][j] = A[i][j] + B[i][j]
	return ans

def minus_matrix(A,B) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*y for i in range(x) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[i][j] = A[i][j] - B[i][j]
	return ans

def transpose_matrix(A) :
	x = len(A)
	y = len(A[0])
	ans = [ [0]*x for i in range(y) ]
	for i in range(0,x) :
		for j in range(0,y) :
			ans[j][i] = A[i][j]
	return ans

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
				for l in range(0,x2) :
					ans[i][j] += A[i][l]*B[l][j]
	return ans


A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2

B2 = transpose_matrix(B)
left = plus_matrix(A,B2)
C2 = power_matrix(C,c)
right = minus_matrix(C2,D)
ans = mul_matrix(left,right) 
print_matrix(ans)