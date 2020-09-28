def det_matrix(A):
	ans = 0
	for i in range(3) :
		x = 1
		for j in range(3) :
			x *= arr[0+j][i+j]
		ans += x
	for i in range(3) :
		y = 1
		for j in range(3) :
			y *= arr[2-j][i+j]
		ans -= y
	return ans

arr = [ [0]*6 for i in range(3) ]
r1,r2,r3 = [],[],[]
r1 = input("Row 1 : ").split()
r2 = input("Row 2 : ").split()
r3 = input("Row 3 : ").split()
for i in range(6) : arr[0][i] = int(r1[i%3])
for i in range(6) : arr[1][i] = int(r2[i%3])
for i in range(6) : arr[2][i] = int(r3[i%3])
print(det_matrix(arr))