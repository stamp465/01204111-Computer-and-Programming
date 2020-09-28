S = int(input("Input starting food (S): "))
P = int(input("Input Paun's eating rate (P): "))
n = int(input("Input Gane's eating rate (n): "))
print(f"Paun eats {S//P} time(s)")
S = S % P
print(f"Gane eats {S//n} time(s)")
S = S % n
print(f"Remaining {S} for dog")