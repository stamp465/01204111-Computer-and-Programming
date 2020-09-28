def upper(tel,big,dam) :
	for i in range(tel) :
		if i==0 or i==tel-1 :
			print(" ",end='')
			print("o"*(big-2),end='')
			print(" ",end='')
		else :
			print("o"*(big),end='')
		print()
	return 

def lower(tel,big,dam) :	
	for i in range(tel) :
		if i > dam+1 and i < tel-1 :
			print(" "*(big//2-dam//2-1),end='')
			print("o"*(dam+2))
		else :
			print(" "*(big//2-dam//2),end='')
			print("o"*dam)
	return 



f = float(input("Input Gold: "))
f //= 1000
if f==0 :
	print("Not enough gold.")
	exit()
dam = int(f)
big = int(f+2)*3
tel = 3+2*int(f)
upper(tel,big,dam)
lower(tel,big,dam)