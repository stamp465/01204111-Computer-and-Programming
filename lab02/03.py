q1 = input("Is Bulotelli injured?(y/n) ")
if q1=='y' : 
	print("Not available")
	exit()
q2 = input("Is Bulotelli late for the training?(y/n) ")
if q2=='n':
	print("Starter")
	exit()
q3 = input("Did Bulotelli perform well in training?(y/n) ")
if q3=='y' : print("Substitute")
else : print("Not selected")