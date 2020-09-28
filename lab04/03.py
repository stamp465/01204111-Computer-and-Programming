liskeep = list()
liscount = list()

def findandcount(lis) :
	maxx = 0
	lenlis = len(lis)
	for i in range(lenlis) :
		if lis[i] in liskeep :
			a = liskeep.index(lis[i])
			liscount[a] += 1;
			if maxx < liscount[a] :
				maxx = liscount[a]
		else :
			liskeep.append(lis[i])
			liscount.append(1)

lis = input("Cards: ").split() 
findandcount(lis)
can = [False] * 4
printcan = ['Mark got "Four of a kind"','Mark got "Full House"','Mark got "Three of a kind"','Mark got "High Card"']
for i in range(len(liscount)) :
	if liscount[i] == 4 :
		can[0] = True
	if liscount[i] == 3 and len(liscount)==2:
		can[1] = True
	if liscount[i] == 3 :
		can[2] = True
can[3] = True
for i in range(len(can)) :
	if can[i] :
		print(printcan[i])
		break