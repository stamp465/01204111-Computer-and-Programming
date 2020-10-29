#Square01.txt
#Square02.txt
#Square03.txt
#Square05.txt

def printS(ss):
	for i in range(len(ss)):
		for j in range(len(ss[i])):
			print(ss[i][j],end='')
		print()

def parseInput(s):
	return s.split('\n') 

def findMaxSquareArea(ss):
	res = 0
	savei = 0
	savej = 0
	for i in range(len(ss)):
		for j in range(len(ss[i])):
			if ss[i][j]=='.':
				start = 0
				#print(i,j)
				while True :
					#print(start)
					check = 0
					if i+start >= len(ss) or j+start >= len(ss[i]):
						res = max(res,(start)**2)
						check = 1
						break
					for k in range(start):
						for l in range(start):
							#if i==2 and j==2 :
								#print(ss[i+k][j+l],end='')
							if ss[i+k][j+l] == '.' :
								pass
							else :
								res = max(res,(start)**2)
								check = 1
								savei = i
								savej = j
						#print()
					if check==1:
						break
					start += 1
	#print(res)
	if res!=0:
		#ss[savei][savej] = 'x'
		for i in range(savei,savei+start):
			ss[savei] = ss[savei][:savej] + 'o'*int(start**(1/2)) + ss[savei][(savej+start):]
		return res,ss
	else :
		return res,ss







fn = input('Enter filename: ')
with open(fn) as f :
	s = f.read()
#print(s)
ss = parseInput(s)
printS(ss)
res,ss = findMaxSquareArea(ss)
print(f'max square area: {res}')
printS(ss)
