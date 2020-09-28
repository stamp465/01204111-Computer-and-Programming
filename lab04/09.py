def med(lis) :
	lis.sort()
	a = len(lis)
	if a%2 == 0:
		return lis[a//2]+lis[a//2-1]
	else :
		return lis[a//2]

lis = list()
while len(lis) != 5 :
	N = input("Enter a positive number: ")
	N = int(N)
	if N > 0 :
		lis.append(N)
print("sum:",sum(lis))
print("min:",min(lis))
print("max:",max(lis))
print("med:",med(lis))