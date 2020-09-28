h = int(input("h: "))
c = input("Character: ")
y = input("Is the tree invert?(y/n): ")
if y=='y' :
	for i in range(0,h//2) :
		for j in range(0,h-1) :
			print(" ",end='')
		print(c)
	for i in range(h*2-1,0,-2) :
		for j in range(0,(h*2-1-i)//2) :
			print(' ',end='')
		for j in range(0,i) :
			print(c,end='')
		print("")
else :
	for i in range(0,h*2-1,+2) :
		for j in range(0,(h*2-1-i)//2) :
			print(' ',end='')
		for j in range(0,i+1) :
			print(c,end='')
		print("")
	for i in range(0,h//2) :
		for j in range(0,h-1) :
			print(" ",end='')
		print(c)