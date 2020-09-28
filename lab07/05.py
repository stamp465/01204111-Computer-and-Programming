#05
def north(x,y,arr) :
	for j in range(y) :
		countt = 0
		maxx = -1
		for i in range(x) :
			if arr[i][j] > maxx :
				countt += 1
				maxx = arr[i][j]
	return countt

def south(x,y,arr) :
	for j in range(y) :
		countt = 0
		maxx = -1
		for i in range(x-1,-1,-1) :
			if arr[i][j] > maxx :
				countt += 1
				maxx = arr[i][j]
	return countt

def west(x,y,arr) :
	for i in range(x) :
		countt = 0
		maxx = -1
		for j in range(y) :
			if arr[i][j] > maxx :
				countt += 1
				maxx = arr[i][j]
	return countt

def east(x,y,arr) :
	for i in range(x) :
		countt = 0
		maxx = -1
		for j in range(y-1,-1,-1) :
			if arr[i][j] > maxx :
				countt += 1
				maxx = arr[i][j]
	return countt

size = input("City Size: ").split()
x = int(size[0])
y = int(size[1])
arr = [ [0]*int(size[1]) for i in range(int(size[0])) ]
for i in range(int(size[0])) :
	arrsize = input().split()
	for j in range(int(size[1])) :
		arr[i][j] = int(arrsize[j])
arrchar = ['N','S','E','W']
arrans = [ north(x,y,arr), south(x,y,arr) , east(x,y,arr) , west(x,y,arr)  ]
for i in range(4) :
	if arrans[i] == max(arrans) :
		print(arrchar[i],end=' ')
