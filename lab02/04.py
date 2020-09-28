enddis = int(input("Distance from starting point(m.): "))
now = int(0)
lis = []
while True :
	if enddis == now : 
		lis.append(now)
		break
	elif enddis > now :
		now += 5
		lis.append(now)
		now -= 2
		if enddis == now : 
			lis.append(now)
			break
		lis.append(now)
	else :
		now -= 4
		lis.append(now)
		now += 3
		if enddis == now : 
			lis.append(now)
			break
		lis.append(now)
print(*lis) 
print(f"Buzz moved {len(lis)//2} set(s)")