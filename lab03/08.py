ToHex = {
	10 : 'A',
	11 : 'B',
	12 : 'C',
	13 : 'D',
	14 : 'E',
	15 : 'F'
}

def Hex(Dec) :
	hex = ''
	while True:
		ch = Dec%16
		a = str(ch)
		if ch>9 :
			a = ToHex[ch]
		hex = a + hex
		Dec //= 16
		if Dec==0 :
			break

	return hex

while True :
	Dec = int(input("Input Decimal: "))
	if Dec == -1 :
		print("Good bye.")
		break
	print("Hex: %s"%(Hex(Dec)))