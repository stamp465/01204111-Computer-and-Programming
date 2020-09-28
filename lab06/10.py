def Substring(text,sub) :
	ans = ""
	arr = []
	i = 0
	while i < len(text) :
		if text[i] == sub[0] :
			if text[i:i+len(sub)] == sub :
				arr.append('['+sub+']')
				i += len(sub)
			else :
				arr.append(text[i])
				i += 1
		else :
			arr.append(text[i])
			i += 1
		

	ans = ans.join(arr)
	return ans

text = input("Text: ")
substring = input("Substring: ")
ans = Substring(text,substring)
print(ans) if ans!=text else print("Not found")