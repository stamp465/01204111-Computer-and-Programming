week = int(input("Estimated time : "))
can = 2.5*week
week = week//8
phy,wei,fit = 0,0,0 
for i in range(week) :
	print("Week%d"%(i+1))
	phy += int(input("Physical therapy : "))
	wei += int(input("Weight training : "))
	fit += int(input("Fitness training : "))
if phy>=can and wei>=can and fit>=can :
	print("Buzzy has recovered in time.")
else : print("Buzzy has not recovered in time.")