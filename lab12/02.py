def gen(ans) :
	check = [0]*7
	anss = ["Grade A",
		"Grade A (Upgrade From B)",
		"Grade B",
		"Grade B (Upgrade From C)",
		"Grade C",
		"Grade C (Upgrade From No Grade)",
		"No Grade"]
	for i in range(0,n):
		for j in range(0,n):
			if ans[i][j] >= 90 : check[1] += 1
			if ans[i][j] >= 85 : check[3] += 1
			if ans[i][j] >= 70 : check[5] += 1
	for i in range(1,n-1):
		for j in range(1,n-1):
			grade = 0
			for x in range(-1,2,+1) :
				for y in range(-1,2,+1) :
					grade += ans[i+x][j+y]
			grade /= 9
			#print(grade)
			if grade >= 85 : check[0] += 1
			if grade >= 70 : check[2] += 1
			if grade >= 60 : check[4] += 1
			if grade < 60 : check[6] += 1
	#print(check)
	if check[0] == (n-2)*(n-2) : return anss[0]
	elif check[2] == (n-2)*(n-2) : 
		if check[1] >= n*n/4 : return anss[1]
		return anss[2]
	elif check[4] == (n-2)*(n-2) : 
		if check[3] >= n*n/4 : return anss[3]
		return anss[4]
	else :
		if check[5] >= n*n/4 : return anss[5]
		return anss[6]
		

n = int(input("Material size: "))
ans = []
for i in range(n) :
	q = input()
	a = q.split()
	ans.append( [int(i) for i in a ])
print("Output:",gen(ans))