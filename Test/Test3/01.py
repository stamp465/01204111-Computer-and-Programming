def printMat(lis) :
	for i in range(len(lis)) :
		for j in range(len(lis[0])) :
			print(f"{lis[i][j]:.2f}",end=' ')
		print()

def plusMat(aa,bb):
	for i in range(len(aa)) :
		for j in range(len(aa[0])) :
			aa[i][j] += bb[i][j]
	return aa

def minusMat(aa,bb):
	for i in range(len(aa)) :
		for j in range(len(aa[0])) :
			aa[i][j] -= bb[i][j]
	return aa

def transMat(aa):
	lis = [ [0.0]*len(aa) for i in range(len(aa[0])) ]
	for i in range(len(aa)) :
		for j in range(len(aa[0])) :
			lis[j][i] = aa[i][j]
	return lis

def NmulMat(aa,x):
	xx = []
	for i in range(len(aa)) :
		ccx = []
		for j in range(len(aa[0])) :
			ccx.append(x*aa[i][j])
		xx.append(ccx)
	return xx

def mulMat(aa,bb):
	return [[ sum(aa[i][k] * bb[k][j] for k in range(len(aa[0]))) for j in range(len(bb[0])) ] for i in range(len(aa))  ]

def mulmulMat(aa,x) :
	xx = []
	for i in range(len(aa)) :
		ccx = []
		for j in range(len(aa[0])) :
			ccx.append(x*aa[i][j])
		xx.append(ccx)
	
	for i in range(x-1) :
		xx = mulMat(xx,aa)
	return xx

def setMat(FileName):
	f = open(FileName)
	r = f.readlines()
	lis = [ i.strip().split() for i in r ]
	for i in range(len(lis)) :
		for j in range(len(lis[0])) :
			lis[i][j] = float(lis[i][j])
	f.close()
	return lis

def sol1(aa,x,cc) :
	return plusMat(transMat(aa),NmulMat(cc,x))

def sol2(a,x) :
	return mulmulMat(a,x)

def sol3(a,b,c) :
	return minusMat( transMat(mulMat(a,b)),c)

def sol4(a,c) :
	return mulMat(c, plusMat(transMat(c),NmulMat(a,2)   )    )

a = setMat('A.txt')
b = setMat('B.txt')
c = setMat('C.txt')


print("Ans 1 = ")
printMat( sol1(a,7,c) )

print("Ans 2 = ")
printMat( sol2(b,3) )

print("Ans 3 = ")
printMat( sol3(a,b,c) )

print("Ans 4 = ")
printMat( sol4(a,c) )