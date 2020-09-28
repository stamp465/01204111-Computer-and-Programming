class MyMath:
	def __init__(self) :
		self.To = {
			10 : 'A',
			11 : 'B',
			12 : 'C',
			13 : 'D',
			14 : 'E',
			15 : 'F'
		}
		self.dec = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] 
		self.roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]

	def is_even(self,num):
		return num%2==0

	def fac(self,num):
		for i in range(1,num):
			num *= i
		return num

	def is_prime(self,num) :
		for i in range(2,num//2) :
			if num%i == 0 :
				return False
		return True

	def divide_by(self,num,k) :
		return num%k==0

	def ten_to_bi(self,num) :
		ans = ''
		while True:
			ch = num%2
			a = str(ch)
			if ch>9 :
				a = self.To[ch]
			ans = a + ans
			num //= 2
			if num==0 :
				break
		return ans
	def ten_to_oct(self,num) :
		ans = ''
		while True:
			ch = num%8
			a = str(ch)
			if ch>9 :
				a = self.To[ch]
			ans = a + ans
			num //= 8
			if num==0 :
				break
		return ans
	def ten_to_sixteen(self,num) :
		ans = ''
		while True:
			ch = num%16
			a = str(ch)
			if ch>9 :
				a = self.To[ch]
			ans = a + ans
			num //= 16
			if num==0 :
				break
		return ans

	def int_to_roman(self,num) :
		lis = []
		for i in range(12,-1,-1) :
			check = num//self.dec[i]
			num %= self.dec[i]
			for j in range(0,check) :
				lis.append(self.roman[i])
		s = ''
		return s.join(lis)

	def pii(N) :	
		total = float(3.00)
		st = 2
		for i in range(N-1) :
			if i%2==0 :
				total += 4/(st*(st+1)*(st+2))
			else :
				total -= 4/(st*(st+1)*(st+2))
			st += 2
		return total
	pi = pii(51)