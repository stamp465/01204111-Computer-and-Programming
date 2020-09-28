#04
def can(subtext,sub,can1) :
	#print(subtext,sub)
	countt = 0
	save = []
	for i in range(len(sub)) :
		if subtext[i] != sub[i] :
			countt += 1
	return True if countt <= can1 else False

def change(subtext,sub) :
	for i in range(len(sub)) :
		if subtext[i] != sub[i] :
			subtext = subtext[:i] + '?' + subtext[i+1:]
	return subtext

def check(text,sub) :
	new = []
	i = 0
	can1 = 1
	if sub in text :
		can1 = 0
	while i < len(text)-2*len(sub) :
		if can(text[i:i+len(sub)],sub,can1) :
			new += '[' + change(text[i:i+len(sub)],sub) + ']'
			i += len(sub)-1
		else :
			new += text[i]
		i += 1
	return new




text = input("Text: ")
sub = input("Substring: ")
for i in range(len(sub)) : text += '  '
print(''.join(check(text,sub)))