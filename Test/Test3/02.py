
def gensky(sky) :
	return [ [0]*sky for i in range(sky) ]

def genboom1(m,sky,x,y):
	#\
	for i in range( -m//2+1,m//2+1 ) :
		if x+i >= 0 and x+i < len(sky) and y+i >= 0 and y+i < len(sky) :
			sky[x+i][y+i] += 1
	#/
	for i in range( -m//2+1,m//2+1 ) :
		if x-i >= 0 and x-i < len(sky) and y+i >= 0 and y+i < len(sky) :
			sky[x-i][y+i] += 1
	#|
	for i in range( -m//2+1,m//2+1 ) :
		if x+i >= 0 and x+i < len(sky) and y >= 0 and y < len(sky)  :
			sky[x+i][y] += 1
	#_
	for i in range( -m//2+1,m//2+1 ) :
		if  y+i >= 0 and y+i < len(sky) and x >= 0 and x < len(sky):
			sky[x][y+i] += 1
	if x >= 0 and x < len(sky) and y >= 0 and y < len(sky) :
		sky[x][y] -= 3
	return sky

def genboom2(m,sky,x,y):
	start = m
	while True :

		for i in range(-start+1,start) :
			if x+i >= 0 and x+i < len(sky) and y-start+1 >= 0 and y-start+1 < len(sky) :
				#print(x+i,y-start+1)
				sky[x+i][y-start+1] += start

		for i in range(-start+1,start) :
			if x+i >= 0 and x+i < len(sky) and y+start-1 >= 0 and y+start-1 < len(sky) :
				#print(x+i,y+start-1)
				sky[x+i][y+start-1] += start


		for i in range(-start+2,start-1) :
			if y+i >= 0 and y+i < len(sky) and x-start+1 >= 0 and x-start+1 < len(sky) :
				sky[x-start+1][y+i] += start

		for i in range(-start+2,start-1) :
			if y+i >= 0 and y+i < len(sky) and x+start-1 >= 0 and x+start-1 < len(sky) :
				sky[x+start-1][y+i] += start

		start -= 1
		if start == 0 : break
	if x >= 0 and x < len(sky) and y >= 0 and y < len(sky) :
		sky[x][y] -= 1
	return sky

def printsky(sky) :
	for i in range(len(sky)) :
		for j in range(len(sky[0])) :
			if sky[i][j] == 0 :
				print('.',end=' ')
			else :
				print(sky[i][j]%10,end=' ')
		print()

k = int(input("Sky : "))
sky = gensky(k)
hanabi = int(input("Hanabi : "))
for i in range(hanabi) :
	a = input()
	lis = a.split()
	x,y,boom,m = int(lis[0]),int(lis[1]),int(lis[2]),int(lis[3])
	if boom == 1 :
		sky = genboom1(m,sky,x,y)
	if boom == 2 :
		sky = genboom2(m,sky,x,y)

printsky(sky)