'''
def arrow_text1(strings,a) :
	for i in range(a,1,-1) :
		for j in range(0,i) :
			print(" ",end='')
		print(strings)
	for i in range(0,a) :
		for j in range(0,i+1) :
			print(" ",end='')
		print(strings)

strings = input("Enter a string: ")
a = 0

while a<=0 :
	a = int(input("Enter a positive integer: "))

print("012345678901234567890123456789")
arrow_text1(strings,a)
'''

'''
def twin_prime1(a) :
	check = 0
	for i in range(2,a//2) :
		if a%i==0 :
			return False
	return True

a = 0
while a<99 or a>9999:
	a = int(input("Enter an integer (99-9999): "))

coo = 0
while True:
	if twin_prime1(a) and twin_prime1(a+2) :
		print("(%d, %d)"%(a,a+2))
		coo += 1
	if coo==5 :
		break
	a += 1


twin_prime1 = [True] *10000000

def sieve() :
	for i in range(2,20000) :
		if twin_prime1[i] :
			for j in range(i+i,1000000,i) :
				twin_prime1[j] = False

sieve()

a = 0
while a<99 or a>9999:
	a = int(input("Enter an integer (99-9999): "))

coo = 0
while True:
	if twin_prime1[a] and twin_prime1[a+2] :
		print("(%d, %d)"%(a,a+2))
		coo += 1
	if coo==5 :
		break
	a += 1
'''