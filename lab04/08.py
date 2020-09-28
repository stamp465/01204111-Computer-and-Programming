def intersect(A,B,string) :
	mi = list()
	for i in range(len(A)) :
		for j in range(len(B)) :
			if A[i] == B[j] :
				if A[i] in mi :
					break
				mi.append(A[i])
				break
			

	if len(mi) != 0 :
		print("%s "%(string),end='')
		for i in range(len(mi)) : print(mi[i],end=" ")
	else :
		print("%s empty set"%(string),end='')
	print()


def minus(A,B,string) :
	mi = list()
	for i in range(len(A)) :
		a = 0
		for j in range(len(B)) :
			if A[i] == B[j] :
				a = 1
				break;
		if a==0 :
			mi.append(A[i])

	if len(mi) != 0 :
		print("%s "%(string),end='')
		for i in range(len(mi)) : print(mi[i],end=" ")
	else :
		print("%s empty set"%(string),end='')
	print()

def union(A,B,string) :
	mi = B
	for i in range(len(A)) : 
		if A[i] in mi :
			pass
		else :
			mi.append(A[i])
	mi.sort()
	if len(mi) != 0 :
		print("%s "%(string),end='')
		for i in range(len(mi)) : print(mi[i],end=" ")
	else :
		print("%s empty set"%(string),end='')
	print()


A2,B2 = list(),list()
A = input("Input setA: ").split()
B = input("Input setB: ").split()
for i in range(len(A)) : A2.append(int(A[i]))
for i in range(len(B)) : B2.append(int(B[i]))
A2.sort()
B2.sort()
intersect(A2,B2,'A intersect B:')
minus(A2,B2,'A minus B:') 
minus(B2,A2,'B minus A:') 
union(A2,B2,'A union B:')