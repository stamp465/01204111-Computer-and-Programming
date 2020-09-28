def openfile_save(file) :
	f = open(file)
	r = f.readlines()
	lis = [ i.strip().split(',') for i in r ]
	return lis
	

def enter_number(lis,n):
	l = len(lis)
	if n == 1 :
		print(l)
	
	elif n == 2 :
		maxx = 0
		summ = [0]*len(lis[0])

		for i in range( len(lis[0])-1 ):
			for j in range(1,l) :
				summ[i] = summ[i] + int(lis[j][i])
			maxx = max(maxx,summ[i])
		for i in range( len(lis[0]) ):
			if summ[i] == maxx :
				#print(maxx)
				print(lis[0][i])

	elif n == 3 :
		for i in range( len(lis[0])-1 ):
			blue = []
			if lis[0][i] == 'blueplanet' :
				for j in range(1,l) :
					blue.append(int(lis[j][i]))
				blue.sort(reverse=True)
				for j in range(3) :
					print(blue[j],end=' ')
				print()


	elif n == 4 :
		maxx = 0
		summ = [0]*l

		for i in range( 1,l ):
			for j in range(len(lis[0])-1) :
				summ[i] = summ[i] + int(lis[i][j])
			maxx = max(maxx,summ[i])

		for i in range( l ):
			if summ[i] == maxx :
				#print(maxx)
				print(lis[i][len(lis[0])-1],maxx)


	elif n == 5 :
		for i in range( len(lis[0])-1 ):
			tvshow = []
			if lis[0][i] == 'tvshow' :
				for j in range(1,l) :
					tvshow.append(int(lis[j][i]))
				tvshow.sort(reverse=True)
				for j in range(1,l) :
					if int(lis[j][i]) == tvshow[0] :
						print(lis[j][len(lis[0])-1],tvshow[0])


	elif n == 6 :
		countt = 0
		for i in range( len(lis[0])-1 ):
			if lis[0][i] == 'korea' :
				for j in range(1,l) :
					if int(lis[j][i]) > 500 :
						countt = countt + 1
		print(countt)

	elif n == 7 :
		savesiam = 0
		savefood = 0
		for i in range( len(lis[0])-1 ):
			if lis[0][i] == 'siam' :
				savesiam = i
			if lis[0][i] == 'food' :
				savefood = i
		countt = 0
		#print(savesiam,savefood,l)
		for i in range( 1, l ):
			if int(lis[i][savesiam]) > int(lis[i][savefood]) :
				countt = countt + 1
		print(countt)

	elif n == 8 :
		maxx = 0
		summ = [0]*l
		a = 0
		for i in range( len(lis[0])-1 ):
			if lis[0][i] == 'rajdumnern' :
				a  = i

		for i in range( 1,l ):
			for j in range(len(lis[0])-1) :
				summ[i] = summ[i] + int(lis[i][j])
			maxx = max(maxx,int(lis[i][a])/summ[i])
		for i in range( 1,l ):
			if int(lis[i][a])/summ[i] == maxx :
				#print(maxx)
				print(lis[i][len(lis[0])-1])


	elif n == 9 :
		maxx = 0
		summ = [0]*l
		countt = 0
		for i in range( 1,l ):
			check = []
			for j in range(len(lis[0])-1) :
				summ[i] = summ[i] + int(lis[i][j])
				check.append(int(lis[i][j]))
			check.sort(reverse=True)
			if (check[0]+check[1])/summ[i] > 0.7 :
				countt = countt + 1
		print(countt)
		

	elif n == 10 :
		countt = 0
		a = 0
		for i in range( len(lis[0])-1 ):
			if lis[0][i] == 'pantip' :
				a  = i

		for i in range( 1,l ):
			if int(lis[i][a]) == 0 :
				countt = countt + 1
		print(countt)

file = input('File name: ')
lis = openfile_save(file)
enter_number( lis , int( input('enter number: ') ) ) 