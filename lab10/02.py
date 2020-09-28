#02
import json
def openjson(name) :
	f = open(name)
	truedata = []
	for s in f :
		ss = json.loads(s)
		truedata.append(ss)
	return truedata

def one(data) :
	return len(data)

def two(data) :
	return len(set([ i['reviewerID'] for i in data ]))

def three(data) :
	return len(set([ i['productID'] for i in data ]))

def four(data) :
	return len(set( [ i['category'].split('>')[0]  for i in data   ]   ))

def five(data) :
	return len(set( [ i['category'].split('>')[1]  for i in data   ]   ))

def six(data):
	reviewer,maxx,ans = {},0,[]
	for i in data :
		if not i['reviewerID'] in reviewer :
			reviewer[ i['reviewerID'] ] = 0
		reviewer[ i['reviewerID'] ] += 1
		maxx = max(maxx,reviewer[ i['reviewerID'] ])
	for i in reviewer :
		if reviewer[i] == maxx :
			ans.append(i)
	for i in ans :
		print(i)

def seven(data) :
	pricer,maxx,savemag,savep = {},0,0,''
	for i in data :
		if not i['productName'] in pricer :
			pricer[ i['productName'] ] = list()
		pricer[ i['productName'] ].append(i['overall'])
	for i in pricer :
		maxx = max(maxx,sum(pricer[i])/len(pricer[i]))
	for i in pricer :
		if sum(pricer[i])/len(pricer[i]) == maxx :
			if savep == '_' : 
				savep = i 
				savemag = len(pricer[i])
			else :
				if len(pricer[i]) > savemag :
					savep = i 
					savemag = len(pricer[i])
	return savep

def eight(data) :
	pricer = {}
	pricerview = {}
	for i in data :
		if not i['productName'] in pricer :
			pricer[ i['productName'] ] = len( i['reviewText'].strip().split() )
			pricerview[ i['productName'] ] = 1
		else :
			pricer[ i['productName'] ] += len( i['reviewText'].strip().split() )
			pricerview[ i['productName'] ] += 1
	maxx = []
	maxxch = 0
	for i in pricer :
		#print(pricer[i],pricerview[i])
		maxxch = max(maxxch, pricer[i]/pricerview[i] )
	for i in pricer :
		if maxxch == pricer[i]/pricerview[i] :
			maxx.append(i)
	for i in maxx :
		print(i)

name = input("file name: ")
data = openjson(name)
iff = int(input("input: "))

if iff==1 :
	print(one(data))
elif iff==2 :
	print(two(data))
elif iff==3 :
	print(three(data))
elif iff==4 :
	print(four(data))
elif iff==5 :
	print(five(data))
elif iff==6 :
	six(data)
elif iff==7 :
	print(seven(data))
elif iff==8 :
	eight(data)
