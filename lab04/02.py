stringg = list()
def striii(nubs) :
	n = int(nubs[0])
	st = 1
	while st < len(nubs) :
		a = int(nubs[st])
		stringg.append(chr(a))
		st += n+1

	return 

nub = input().split() 
striii(nub)
for i in range(len(stringg)) :
	print(stringg[i],end='')