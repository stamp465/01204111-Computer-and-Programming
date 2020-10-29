Plat = dict()
Lisen = dict()
Version = dict()
github = dict()
githubstar = dict()
python = {
	'python' : 0,
	'nub' : 0
}
JS = {
	'nub' : 0
}
saveLanguage = dict()
saveEnd = dict()
class Data :
	def __init__(self,Name,Platform,License,NbOfVersion,Language,Host,Size,Stars,ReadmeFilename) :
		self.Name = Name
		self.Platform = Platform
		self.License = License
		self.NbOfVersion = NbOfVersion
		self.Language = Language
		self.Host = Host
		self.Size = Size
		self.Stars = Stars
		self.ReadmeFilename = ReadmeFilename

		if self.Platform not in Plat :
			Plat[ self.Platform ] = 1
		else :
			Plat[ self.Platform ] += 1

		if self.License not in Lisen :
			Lisen[ self.License ] = 1
		else :
			Lisen[ self.License ] += 1

		if self.Language not in saveLanguage :
			saveLanguage[ self.Language ] = 1
		else :
			saveLanguage[ self.Language ] += 1

		Version[self.Name] = float(NbOfVersion)
		if self.Language == 'Python' :
			python[ 'python' ] += float(Size)
			python[ 'nub' ] += 1

		if self.Host == 'GitHub' :
			if self.Language not in github :
				github[ self.Language ] = 1
			else :
				github[ self.Language ] += 1

		if self.Host == 'GitHub' :
			githubstar[ self.Name ] = int(Stars)

		if Name.find("js") != -1 :
			JS[ 'nub' ] += 1
		elif Name.find("jS") != -1 :
			JS[ 'nub' ] += 1
		elif Name.find("Js") != -1 :
			JS[ 'nub' ] += 1
		elif Name.find("JS") != -1 :
			JS[ 'nub' ] += 1

		checkEnd = ReadmeFilename.find('.')
		if ReadmeFilename[checkEnd:] not in saveEnd :
			saveEnd[ ReadmeFilename[checkEnd:] ] = 1
		else :
			saveEnd[ ReadmeFilename[checkEnd:] ] += 1



def readfile(name) :
	data = []
	f = open(name)
	r = f.readlines()
	lis = [ i.strip().split(',') for i in r ]
	for i in range(1,len(lis)) :
		#print(lis[i])
		data.append( Data(lis[i][0],lis[i][1],lis[i][2],lis[i][3],lis[i][4],lis[i][5],lis[i][6],lis[i][7],lis[i][8])  )
	return data

def NubPlatform(Plat) :
	return len(Plat)

def MostPlatform(Plat) :
	P = sorted(Plat,key=Plat.get)
	return P[len(P)-1],P[len(P)-2]

def NubLicense(Lisen) :
	return len(Lisen)

def MostLicense(Lisen) :
	P = sorted(Lisen,key=Lisen.get)
	return P[len(P)-1],P[len(P)-2]

def MostVersion(Version) :
	P = sorted(Version,key=Version.get)
	return P[len(P)-1]

def VerofMostVersion(Version) :
	P = sorted(Version,key=Version.get)
	return Version[P[len(P)-1]]

def LessLangue(github) :
	P = sorted(github,key=github.get)
	ans = []
	for i in P :
		if github[i] == github[P[0]] :
			ans.append(i)
	return ans

def MostStar(githubstar,data) :
	P = sorted(githubstar,key=githubstar.get)
	ans = []
	for i in P :
		if githubstar[i] == githubstar[P[len(P)-1]] :
			ans.append(i)
	#print(githubstar[P[len(P)-1]])
	savelen = {}
	saveLisen = {}
	for i in ans :
		for j in data :
			if j.Name == i :

				if j.Language in savelen :
					savelen[j.Language] += 1
				else :
					savelen[j.Language] = 1

				if j.License in saveLisen :
					saveLisen[j.License] += 1
				else :
					saveLisen[j.License] = 1

	A = sorted(savelen,key=savelen.get)
	B = sorted(saveLisen,key=saveLisen.get)
	return A[len(A)-1],B[len(B)-1]

def CheckEndNotMD(saveEnd) :
	nub = 0
	for i in saveEnd :
		if i != '.md' and i!= '.markdown' and i!= '.mkd' :
			nub += 1
	return nub

name = 'out1.csv'
data = readfile(name)

print("1.1 Number of Platform = ",NubPlatform(Plat))
print("1.2 Top 2 of Platform = ",MostPlatform(Plat))
print("2.1 Number of License = ",NubLicense(Lisen))
print("2.2 Top 2 of License = ",MostLicense(Lisen))
print("3.1 Most of Version = ",VerofMostVersion(Version))
print("3.2 That Project = ",MostVersion(Version))
print(f"4.1 Avg Size = {python['python']/python['nub']:.3f} MB")
print(f"5.1 Less Language = {LessLangue(github)} \n Number of Less Language = {len(LessLangue(github))} Language")
print(f"5.2 แต่ละภาษาใช้งานไปภาษาละ = {github[ LessLangue(github)[0]   ]} โปรเจค รวมกันเป็น {len(LessLangue(github))*github[LessLangue(github)[0]] } โปรเจค")
print(f"6. มีอีกทั้งหมด = {CheckEndNotMD(saveEnd)} สกุล ที่ไม่ใช่ .markdown .md .mkd")
#print(saveEnd,len(saveEnd))
print("7.1 มักใช้ภาษา = ",MostStar(githubstar,data)[0])
print("7.2 มักใช้license = ",MostStar(githubstar,data)[1])
print("8. เกี่ยวกับ JS = ",JS['nub'])
