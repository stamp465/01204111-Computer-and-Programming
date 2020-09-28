def anytoten(any,n):
	n = int(n)
	anyy = 0
	co = len(any)
	for i in range(0,co) :
		if ord(any[i]) >= 65 :
			anyy += (ord(any[i])-55)*(n**(co-1-i))
		else :
			anyy += int(any[i])*(n**(co-1-i))
	return anyy

def tentoany(ten,m):
	m = int(m)
	tenn = []
	while True :
		a = ten%m
		ten//=m
		#print("mod %d to %d"%(a,ten))
		if(a>9) :
			tenn.append(chr(a+55))
		else :
			tenn.append(str(a))
		if ten < m :
			if(ten>9) :
				tenn.append(chr(ten+55))
			else :
				tenn.append(str(ten))
			break;
	tenn = tenn[::-1]
	strten = ""
	strten = strten.join(tenn)
	return strten

n = input()
m = input()
string = input()
ten = anytoten(string,n)
#print(ten)
any = tentoany(ten,m)
print(any)