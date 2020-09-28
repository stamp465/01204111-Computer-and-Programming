#01
lis = []
while True :
	a = int(input())
	if a==0 :
		break
	lis.append(a)
lis.reverse()
print(*lis)