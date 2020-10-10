def printf(ans):
	for i in range(len(ans)) :
		for j in range(len(ans[i])) :
			print(ans[i][j],end=' ')
		print()

not_O = { # /
	'/' : {
		'up' : 'right',
		'right' : 'up',
		'down' : 'left',
		'left' : 'down'
	},
	'\\' : {
		'up' : 'left',
		'left' : 'up',
		'down' : 'right',
		'right' : 'down'
	}
}

goto = {
	'up' : [1,0],
	'right' : [0,-1],
	'down' : [-1,0],
	'left' : [0,1]
}

def startatup(ans) :
	maxx = 0

	m = 0
	for s in range(1,len(ans[1])-1) :
		status = 'up'
		can = 0
		i = 1
		j = s
		while ans[i][j] != 'x' :
			if ans[i][j] != 'O' :
				can += 1
				status = not_O[ ans[i][j] ][ status ]
				i += goto[status][0]
				j += goto[status][1]
			else :
				i += goto[status][0]
				j += goto[status][1]
		maxx = max(can,maxx)
		m = max(m,can)
	print(status,m)

	m = 0
	for s in range(1,len(ans[1])-1) :
		status = 'down'
		can = 0
		i = len(ans) - 2
		j = s
		while ans[i][j] != 'x' :
			if ans[i][j] != 'O' :
				can += 1
				status = not_O[ ans[i][j] ][ status ]
				i += goto[status][0]
				j += goto[status][1]
			else :
				i += goto[status][0]
				j += goto[status][1]
		maxx = max(can,maxx)
		m = max(m,can)
	print(status,m)

	return maxx

def startatright(ans) :
	maxx = 0

	m = 0
	for s in range(1,len(ans)-1) :
		status = 'right'
		can = 0
		i = s
		j = len(ans[1])-2
		while ans[i][j] != 'x' :
			if ans[i][j] != 'O' :
				can += 1
				status = not_O[ ans[i][j] ][ status ]
				i += goto[status][0]
				j += goto[status][1]
			else :
				i += goto[status][0]
				j += goto[status][1]
		maxx = max(can,maxx)
		m = max(m,can)
	print(status,m)

	m = 0
	for s in range(1,len(ans)-1) :
		status = 'left'
		can = 0
		i = s
		j = 1
		while ans[i][j] != 'x' :
			if ans[i][j] != 'O' :
				can += 1
				status = not_O[ ans[i][j] ][ status ]
				i += goto[status][0]
				j += goto[status][1]
			else :
				i += goto[status][0]
				j += goto[status][1]
		maxx = max(can,maxx)
		m = max(m,can)
	print(status,m)

	return maxx

ans = []
t = 0
while True :
	q = input()
	if q=='' : 
		ans.append(  ['x']*(len(ans[0]))   )
		break
	if t==0 : ans.append(  ['x']*(len(q.split())+2)   )
	ans.append( ['x'] + q.split() + ['x'])
	t += 1
#printf(ans)
anss = 0
anss = max( startatup(ans) ,startatright(ans) )
print("Maximum saitron is %d particle(s)"%(2**anss))