a = str(input())
i = 0
while True :
	b = str(input())
	if a[i] == b :
		if i==len(a)-1 :
			print("Succeed!!")
			break
	else :
		print("Fail!!")
		break
	if i==len(a)-1 :
		print("Fail!!")
		break
	i += 1