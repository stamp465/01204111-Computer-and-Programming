def openfile_save(file) :
	with open(file) as f :
		s = f.readlines()
		lists = [ i.strip().split(' ') for i in s if i.strip()!='' ]
	return lists

def findmaxandprint(std) :
	maxx = 0
	summ = [0]*len(std)
	for i in range(len(std)) :
		maxc = int(-1) 
		minc = 1e9
		for j in range(1,len(std[i])) :
			summ[i] = summ[i] + int(std[i][j])
			maxc = max(int(std[i][j]),maxc)
			minc = min(int(std[i][j]),minc)
		maxx = max(summ[i]-maxc-minc,maxx)
		summ[i] = summ[i]-maxc-minc
	print(maxx)
	for i in range(len(std)) :
		if summ[i] == maxx :
			print(std[i][0])


file = input('File name: ')
std = openfile_save(file) 
#print(std)
findmaxandprint(std)

