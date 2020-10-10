
def gen(arr) :
	minn = 1e9
	for i in range(0,len(arr)-1) :
		for j in range(0,len(arr[i])-1) :
			#print(i,j,arr[i][j],arr[i][j+1]*1.1,arr[i+1][j+1]*1.1,arr[i+1][j]*1.1*1.1)
			minn = min(minn,arr[i][j]+arr[i][j+1]*1.1+arr[i+1][j+1]*1.1+arr[i+1][j]*1.1*1.1)
	for i in range(1,len(arr)) :
		for j in range(0,len(arr[i])-1) :
			#print(i,j,arr[i][j],arr[i][j+1]*1.1,arr[i+1][j+1]*1.1,arr[i+1][j]*1.1*1.1)
			minn = min(minn,arr[i][j]+arr[i][j+1]*1.1+arr[i-1][j+1]*1.1+arr[i-1][j]*1.1*1.1)
	return minn

arr = []
while True:
	q = input()
	if q=='' : break
	a = q.split()
	arr.append( [int(i) for i in a ])
check = 0
for i in range(1,len(arr)) :
	if len(arr[i]) != len(arr[i-1]) :
		print("Can't Buy")
		check = 1
		break;
if check == 0 :
	print(f'{gen(arr):.2f}')
