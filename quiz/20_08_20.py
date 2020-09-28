
'''
#1
def printt(ans) :
	if len(ans) == 0 :
		print("A minus B: empty set")
	else :
		print(f"A minus B: {ans}")

def minus(a,b) :
	Set_Minus = []
	lena = len(a)
	lenb = len(b)
	for i in range(0,lena) :
		if a[i] in b :
			pass
		else :
			Set_Minus.append(int(a[i]))
	return Set_Minus

a = input("Input set A: ").split()
b = input("Input set B: ").split()
ans = minus(a,b)
printt(ans)
'''


'''
#2
def printt(ans) :
	if len(ans) == 0 :
		print("A union B: empty set")
	else :
		print(f"A union B: {ans}")

def sortt(a) :
	lena = len(a)
	for i in range(0,lena) :
		for j in range(i+1,lena) :
			if a[i] > a[j] :
				a[i],a[j] = a[j],a[i]
	return a


def union(a,b) :
	Set_union = []
	lena = len(a)
	lenb = len(b)
	for i in range(0,lena) :
		if a[i] in b :
			pass
		else :
			Set_union.append(int(a[i]))
	for i in range(0,len(b)) :
		Set_union.append(int(b[i]))
	return sortt(Set_union)

a = input("Input set A: ").split()
b = input("Input set B: ").split()
ans = union(a,b)
printt(ans)
'''
