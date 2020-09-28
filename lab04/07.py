def gen(n):
	lenn = len(n)
	anslis = list()
	for i in range(lenn) :
		for j in range(i+1,lenn) :
			ans = int(n[i])+int(n[j])
			if ans in anslis :
				continue
			if abs(ans) > 100 :
				continue
			anslis.append(ans)
	return anslis
n = input("Input: ").split()
a = gen(n)
a.sort()
for i in range(len(a)) : print(a[i],end=' ')