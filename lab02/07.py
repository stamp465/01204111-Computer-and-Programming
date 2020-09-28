q1 = input("What's the result of Manchester city's match? ")
q2 = input("What's the result of Liverpool's match? ")
if(q1!=q2) :
	if(q1=='won') : print("Manchester city is the champion of Premier League.")
	else : print("Liverpool is the champion of Premier League.")
	exit()
q3 = int(input("What is the margin that Manchester city won by? "))
q4 = int(input("What is the margin that Liverpool won by? "))
if(q3>q4) :
	print("Manchester city is the champion of Premier League.")
elif(q3<q4) :
	print("Liverpool is the champion of Premier League.")
else :
	q5 = input("Which team won the play-off match?(Manchester city/Liverpool) ")
	if(q5=='Manchester city') :
		print("Manchester city is the champion of Premier League.")
	else :
		print("Liverpool is the champion of Premier League.")