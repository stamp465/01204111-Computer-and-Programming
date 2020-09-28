#06
class py_solution :
	def __init__(self,vongleb) :
		self.vongleb = vongleb
		self.vonglebped = ['(','[','{']
		self.vonglebpid = [')',']','}']
		#print(self.vongleb)

	def is_valid_parentheses(self) :
		checkvongleb = []
		for i in self.vongleb :
			#print(i)
			if i in self.vonglebped :
				checkvongleb.append(i)
			else :
				if len(checkvongleb) == 0 :
					return False
				elif checkvongleb[len(checkvongleb)-1] == self.vonglebped[self.vonglebpid.index(i)] :
					checkvongleb = checkvongleb[:-1]
				else :
					return False
		if len(checkvongleb) != 0 : return False
		return True 

A = input('input: ')
strings = py_solution(A)
if strings.is_valid_parentheses() :
	print('valid parentheses')
else :
	print('invalid parentheses')