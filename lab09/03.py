class Matrix :
	def __init__(self,matrix) :
		self.data = matrix
		#print(self.data)

	def show(self) :
		for i in range(len(self.data)) :
			for j in range(len(self.data[i])) :
				print(f'{self.data[i][j]:^6}', end = ' ') 
			print()

	def plus(self,eny):
		A = self.data 
		B = eny.data
		ans = [  [A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
		return Matrix(ans)

	def minus(self,eny):
		A = self.data 
		B = eny.data
		ans = [  [A[i][j] - B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
		return Matrix(ans)

	def multiply(self,eny) :
		A = self.data 
		B = eny.data
		ans = [ [ sum( A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A)) ]
		return Matrix(ans)

	def det(self) :
		ans = 0
		datadet = []
		for i in range(len(self.data)) :
			dett = []
			for j in range(len(self.data[i])) :
				dett.append(self.data[i][j])
			for j in range(len(self.data[i])) :
				dett.append(self.data[i][j])
			datadet.append(dett)
		redatadet = []
		for i in range(len(self.data)-1,-1,-1) :
			redatadet.append(datadet[i])
		for j in range(len(self.data[i])) :
			aa = 1
			for i in range(len(self.data)) :
				aa *= datadet[i][j+i]
			ans += aa
		for j in range(len(self.data[i])) :
			aa = 1
			for i in range(len(self.data)) :
				aa *= redatadet[i][j+i]
			ans -= aa
		return ans
