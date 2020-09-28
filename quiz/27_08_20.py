
'''
#01
def counttans(string) :
	dic = ['a','e','i','o','u']
	countt = [0]*5
	string = string.lower()
	for i in string :
		if i in dic :
			countt[dic.index(i)] += 1
	return countt,dic

while True:
	string = input("Enter message: ")
	if string == '' : break
	countt,dic = counttans(string)
	for i in range(len(dic)) :
		if countt[i] > 0 :
			print("%s: %d"%(dic[i],countt[i]))
print("Exiting the program.")
'''



#02
nub = float(0)
countt = 0
while True:
	string = input("Enter message: ")
	if string == '' : break
	kg = float(string)
	nub += kg
	if nub > 200 :
		nub = kg
		countt += 1
if nub > 0 :
	countt += 1
print("Elevator works %d time(s)."%countt)
