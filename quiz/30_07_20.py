'''
nub = 0
while True:
	a = int(input())
	if a==0:
		break
	if a > 0 :
		nub += 1
print("I found %d positive integer(s)."%(nub)) if nub > 0 else print("No positive input!")
'''

'''
nub_plus = 0
nub_neg = 0
plus = 0
neg = 0
while True:
	a = int(input("Enter an integer [or 0 to end]: "))
	if a==0:
		break
	if a > 0 :
		nub_plus += 1
		plus += a
	if a < 0 :
		nub_neg += 1
		neg += a
if nub_plus == 0 and nub_neg == 0 :
	print("Nothing else..")
if nub_plus > 0 :
	print("average+: %.2f"%(plus/nub_plus))
if nub_neg > 0 :
	print("average-: %.2f"%(neg/nub_neg))
'''
