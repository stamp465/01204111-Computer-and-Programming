def check(ans) :
	for x in range(0,n) :
		for y in range(0,n) :
			if ans[x][y] == 0 :
				return False
	return True

def zigzag(aa):
	if aa == 1 :
		return 1,[1]
	n = aa
	ans = [ [0]*n for i in range(n)]
	starti = n-1
	startj = 0
	now = 1
	zigup = True 
	while True :
		if zigup == True :
			ans[starti][startj] = now
			starti -= 1
			startj -= 1
			now += 1
			if starti < 0 or startj < 0 :
				zigup = False
				starti += 1
				startj += 1
				if starti - 1 >= 0 :
					starti -= 1
				else :
					startj += 1
		else :	
			ans[starti][startj] = now
			starti += 1
			startj += 1
			now += 1
			if starti >= n or startj >= n :
				zigup = True
				starti -= 1
				startj -= 1
				if startj + 1 < n :
					startj += 1
				else :
					starti -= 1
		if check(ans) == True :
			break	
	return 0,ans

def printf(ch,ans):
	if ch==1 :
		print(f'{ans[0]:3.0f}',end=' ')
	else :
		for x in range(0,n) :
			for y in range(0,n) :
				print(f'{ans[x][y]:3.0f}',end=' ')
			print()
n = int(input())
ch,ans = zigzag(n)
printf(ch,ans)