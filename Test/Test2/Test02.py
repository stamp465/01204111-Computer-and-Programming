#Minisodoku01.txt
#Minisodoku02.txt
#Minisodoku06.txt
def readMiniSodoku(file):
	f = open(file)
	a = f.readlines()
	sodokulis = [ i.strip().split(',') for i in a ]
	#print(sodokulis)
	return sodokulis

def printMiniSodoku(a) :
	res, n = '', len(a)
	for i in range(n):
		for j in range(n) :
			res += f'{a[i][j]:3}'
		if i < n-1 :
			res += '\n'
	print(res)

def printMiniSodoku2(a) :
	res, n = '', len(a)
	al = n**(1/2)
	for i in range(n):
		res += f'{a[i]:3}'
		if i%al+1 == al :
			res += '\n'
	print(res.strip())

def subsudoku(s,g):
	allgroup = g
	linegroup = int(g**(1/2))
	#print(allgroup,linegroup)
	dic = [ [] for i in range(allgroup+5) ]
	n = len(s)
	subg = 1
	check=0
	for i in range(n):
		for j in range(n) :
			#print(dic[subg+(j//linegroup)])
			#print(subg+(j//linegroup))
			dic[ subg+(j//linegroup)  ].append(s[i][j])
		check += 1
		if check==linegroup:
			subg += linegroup
			check = 0
	#print(dic)
	return dic

def checksamein(s):
	xx = len(s)
	#print(s)
	for i in range(xx):
		for j in range(i):
			if i!=j and s[i]==s[j]:
				return False
	return True

def checksameout(s,ss,allgroup):
	count = 0
	for i in range(1,allgroup+1):
		if ss[i] == s :
			count += 1
		#print(s,i,count)
		if count > 1 :
			return False
		
	return True

def checkMiniSodoku(s):
	g = int(len(s)**(1/2))
	allgroup = g*g
	subsudo = subsudoku(s,g*g)
	checkf = True
	saves = 0
	fail = 0
	for i in range(1,allgroup+1) :
		#print()
		if not checksamein(subsudo[i]) :
			checkf = False
			saves = i
			fail = 1
			break
	if checkf :
		for i in range(1,allgroup+1) :
			if not checksameout(subsudo[i],subsudo,allgroup) :
				checkf = False
				saves = i
				fail = 2
				break
	if checkf :
		pass
		#print(checkf)
	else :
		print('Subgrid')
		printMiniSodoku2(subsudo[saves])
		print("fails test#%d!"%(fail))
		#print(checkf)
	return checkf

'''
fn = input('Enter minisodoku0X.txt: ')
s = readMiniSodoku(fn)
#print(s)
print('running miniSodoku')
printMiniSodoku(s)
res = checkMiniSodoku(s)
print(res)
'''
