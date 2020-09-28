change = {
	'A' : 'U',
	'C' : 'G',
	'G' : 'C',
	'T' : 'A'
}
start = 'AUG'
end = ['UAA','UGA','UAG']
def rna(dna) :
	arr = []
	string = ''
	for i in range(len(dna)) :
		arr.append(change[str(dna[i])])
	return string.join(arr)

def amino(rna) :
	nub = 0
	now = 0
	i = 0
	while i < len(rna) :
		if rna[i:i+3] == start and now == 0:
			now = 1
		if now == 1 and rna[i:i+3] in end :
			break;
		if now == 1 :
			nub += 1
			i += 3
		if now == 0 :
			i += 1
	return nub


DNA = input("DNA: ")
RNA = rna(DNA)
print("%d Amino acid(s)"%(amino(RNA)))