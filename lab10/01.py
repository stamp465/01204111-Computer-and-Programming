#01
import json

def openjson(name) :
	f = open(name)
	s = f.read()
	s = s.replace('\t','')
	s = s.replace('\n','')
	s = s.replace(',}','}')
	s = s.replace(',]',']')
	data = json.loads(s)
	truedata = []
	for i in data :
		#print(i)
		truedata.append(i)
	return truedata
	
def allcountry(data) :
	return len(data)

def population(data) :
	return sum( [ int(i['population']) for i in data ] )

def three(data) :
	country1 = [ i['country'] for i in data if i['country'][0] == 'C' ]
	country2 = [ i['country'] for i in data if len(i['country']) > 5 ]
	return len(country1),len(country2)

def four(data) :
	country1 = [ i for i in data if int(i['population']) > 500000000 ]
	country2 = [ i for i in data if int(i['population']) > 250000000 and int(i['population']) < 750000000 ]
	country3 = [ i for i in data if int(i['population']) < 10000000 ]
	return len(country1),len(country2),len(country3)

def five(data) :
	allpop = [ float(i['World']) for i in data  ]
	return sum(allpop[0:20]),sum(allpop[49:150])


name = input("File Name: ")
data = openjson(name)
iff = int(input("Input : "))
if iff==1 :
	print(allcountry(data))
elif iff==2 :
	print(population(data))
elif iff==3 :
	a,b = three(data)
	print(a)
	print(b)
elif iff==4 :
	a,b,c = four(data)
	print(a)
	print(b)
	print(c)
elif iff==5 :
	a,b = five(data)
	print("%.2f"%(a*100))
	print("%.2f"%(b*100))