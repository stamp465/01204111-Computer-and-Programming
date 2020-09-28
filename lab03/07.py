Par = {
	"Ea": -2,
	"Bi": -1,
	"Pa": 0,
	"Bo": 1,
	"DB": 2
}
ans = 0
lis = []
lis2 = []
lis = input().split() 
lis2 = input().split()
for i in range(0,9) :
	ans += int(lis[i]) + int(Par[str(lis2[i])])
print(ans)