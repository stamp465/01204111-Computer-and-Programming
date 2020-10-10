def gen(ans):
	for i in range(len(ans)) :
		for j in range(len(ans[i])) :
			if i==j : ans[i][j] = 1
			if i==n//2 : ans[i][j] = 1
			if j==n//2 : ans[i][j] = 1
			if i+j == n-1 : ans[i][j] = 1
	return ans

def printf(ans):
	for i in range(len(ans)) :
		for j in range(len(ans[i])) :
			if ans[i][j] == 0 : print(' ',end='')
			else : print('+',end='')
		print()


n = int(input("n: "))
ans = [ [0]*n for i in range(n)]
ans = gen(ans)
printf(ans)