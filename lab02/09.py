count = 1
n = 1
sum = 0
a = []
j = 1
while n != 0:
    n = int(input())
    a.append(n)

num_max = 0
countmax = 0
count_list = []
max_list = []

for i in range(len(a)-1) :
    if a[i] == a[j] :
        count += 1
        j += 1
    else :
        if count != 0 :
            count_list.append(count)
            max_list.append(a[i])
        count = 1
        j = j + 1

#print(count_list)
#print(max_list)

findmaxx = 0;
for i in range(len(count_list)) :
	if count_list[i]>findmaxx : 
		findmaxx = count_list[i]
for i in range(len(count_list)) :
	if count_list[i]==findmaxx : 
		print(count_list[i])
		print(max_list[i])
		break;