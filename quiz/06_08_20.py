'''
def pii(N) :	
	total = float(3.00)
	st = 2
	for i in range(N-1) :
		if i%2==0 :
			total += 4/(st*(st+1)*(st+2))
		else :
			total -= 4/(st*(st+1)*(st+2))
		st += 2
	return(total)

N = int(input("n: "))
print("PI: %.10f"%pii(N))
'''

'''
liskeep = list()
liscount = list()

def findandcount(lis) :
	maxx = 0
	lenlis = len(lis)
	for i in range(lenlis) :
		if lis[i] in liskeep :
			a = liskeep.index(lis[i])
			liscount[a] += 1;
			if maxx < liscount[a] :
				maxx = liscount[a]
		else :
			liskeep.append(lis[i])
			liscount.append(1)
	return maxx

lis = input("Enter list of numbers: ").split() 
maxx = findandcount(lis)
#print(lis)
#print(liskeep)
#print(liscount)
for i in range(len(liskeep)) :
	if liscount[i] == maxx :
		print(liskeep[i])
'''