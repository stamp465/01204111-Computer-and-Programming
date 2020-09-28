#03
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

def one(data) :
	return len(data)

def two(data) :
	return len(set([ i['author'] for i in data ]))

def three(data) :
	truedata,maxx,savemax = {},0,[]
	for i in data :
		if not i['author'] in truedata : truedata[ i['author'] ] = 0
		truedata[ i['author'] ] += 1
		maxx = max(maxx,truedata[ i['author'] ])
	for i in truedata :
		if truedata[i] == maxx :
			savemax.append(i)
	for i in savemax :
		print(i)

def four(data) :
	truedata = {}
	for i in data :
		if not i['topic'] in truedata :
			truedata[ i['topic'] ] = 0
		truedata[ i['topic'] ] += 1
	return len(truedata)

def five(data) :
	return len( [ i['topic_priority'] for i in data if  i['topic_priority'] == 'ALERT' ] )

def six(data):
	return len( [ i['topic_priority'] for i in data if  i['topic_priority'] == 'UNIMPORTANT' ] )

def seven(data) :
	return False if len( [ i['language'] for i in data if  i['language'] == 'EN' ] ) == len(data) else True

def eight(data) :
	return max( [ len( i['text'].strip().split() ) for i in data  ] )

name = input("File name: ")
data = openjson(name)
iff = int(input("input: "))

if iff==1 :
	print(one(data))
elif iff==2 :
	print(two(data))
elif iff==3 :
	three(data)
elif iff==4 :
	print(four(data))
elif iff==5 :
	print(five(data))
elif iff==6 :
	print(six(data))
elif iff==7 :
	print(seven(data))
elif iff==8 :
	print(eight(data))