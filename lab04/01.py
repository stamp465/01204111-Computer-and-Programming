Alphabet,Number,Special = list(),list(),list()

def findfu(strings) :
	for i in range(len(strings)) :
		if 65 <= ord(strings[i]) <= 90 or 97 <= ord(strings[i]) <= 122 :
			Alphabet.append(strings[i])
		else :
			if 57 >= ord(strings[i]) >= 48 :
				Number.append(strings[i])
			else :
				Special.append(strings[i])
	return 

string = input().split() 	
findfu(string)	
print("Alphabet:",Alphabet)
print("Number:",Number)
print("Special:",Special)