#01

def zigzag(row,string) :
	maxx = len(string)
	arr = [ [' ']*(maxx) for i in range(row) ]
	
	now = 0
	i = 0
	j = 0
	zig = False
	while True :
		if zig :
			arr[i][j] = string[now]
			i -= 1
			j += 1
			if i==0 :
				zig = False
		else :
			arr[i][j] = string[now]
			i += 1
			if i==row :
				zig = True
				j += 1
				i -= 2
		now += 1
		if now == maxx : break
	return arr



string = input("Input sentence: ")
row = int(input("Input row: "))
arr = zigzag(row,string)
for i in range(row) :
	for j in range(len(string)) :
		if arr[i][j] != ' ' : print(arr[i][j],end='')
