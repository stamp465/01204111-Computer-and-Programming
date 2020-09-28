def openfile_save(file) :
	with open(file,encoding='utf-8') as f :
		a = f.read().split('\n')
		#print(a)
	lis = [ i.split(' ')   for i in a ]
	#print(lis)
	with open(file,encoding='utf-8') as f :
		b1 = []
		b = f.read()
		for i in range(len(b)) :
				if b[i] == '.' and i != len(b)-1 :
					#print(ord(b[i+1]))
					if ord(b[i+1]) >= 48 and  ord(b[i+1])<= 57 and ord(b[i-1]) >= 48 and  ord(b[i-1])<= 57 :
						pass
					else :
						b1.append(0)
				if b[i] == '.' and i == len(b)-1 :
					b1.append(0)
		#print(b1)
	return b1,a,lis


file = input('File name: ')
b,a,lis = openfile_save(file) 


summ = 0
for i in range(len(lis)) :
	summ = len(lis[i])
print("There are %d sentences and %d words."%(len(b),summ))