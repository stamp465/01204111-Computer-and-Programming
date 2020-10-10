
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

def walk(statu, N, ans, starti, startj):
	m = 0
	#print(statu,end=' ')
	for s in range(1,N-1) :
		status = statu
		can = 0
		i = starti
		j = startj
		if starti == -1 : i = s
		if startj == -1 : j = s
		while ans[i][j] != 'x' :
			if ans[i][j] != 'O' :
				can += 1
				status = not_O[ ans[i][j] ][ status ]
				i += goto[status][0]
				j += goto[status][1]
			else :
				i += goto[status][0]
				j += goto[status][1]
		m = max(can,m)
	#print(m)
	return m

def start(ans) :
	maxx = 0

	maxx = max( maxx , walk('up', len(ans[1]), ans, 1, -1  )  )
	maxx = max( maxx , walk('down', len(ans[1]), ans, len(ans) - 2, -1  )  )
	maxx = max( maxx , walk('right', len(ans), ans, -1, len(ans[1]) - 2  )  )
	maxx = max( maxx , walk('left', len(ans), ans, -1, 1  )  )
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
anss = start(ans)
print("Maximum saitron is %d particle(s)"%(2**anss))


