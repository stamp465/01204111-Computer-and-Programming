#04 ***
def upper(n) :
	for i in range(n*2+1,0,-2) :
		print(" ",end='')
		if i == 1 :
			print(' ' * ((n*2+1-i)//2) ,end='')
			print(" =",end='')
			print()
			continue
		print(" " * ((n*2+1-i)//2) ,end='')
		print("="*(i+2))

		print(" ",end='')
		print(" " * ((n*2+1-i)//2),end='')
		print("=",end='')
		print("#" * (i),end='')
		print("=")
	
def lower(n) :
	a =  n//2
	for i in range(1,a*2+1,+2) :
		print(" ",end='')

		print(" " * ((n*2+1-i)//2),end='')
		print("=",end='')
		print("#" * (i),end='')
		print("=",end='')

		if i<a*2-1 :
			print()
			print(" ",end='')

			print(" " * ((n*2+1-i)//2) ,end='')
			print("=" * (i+2))

N = int(input("n: "))
upper(N)
lower(N)