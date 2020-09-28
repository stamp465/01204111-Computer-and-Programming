Grade =	{
  "A": 4.0,
  "B+": 3.5,
  "B": 3.0,
  "C+": 2.5,
  "C": 2.0,
  "D+": 1.5,
  "D": 1.0
}
GPA = float(0)
Total = float(0)
N = int(input("How many subject: "))
for i in range(N) :
	a = float(input("Subject %d Credits: "%(i+1)))
	b = input("Subject %d Grade: "%(i+1))
	#print("%.2f %s %.2f"%(a,b,Grade[b]))
	Total += a
	GPA += Grade[b]*a
	#print("%.2f %.2f"%(GPA,Total))
print("Output: Total Credit = %.1f ,GPA = %.2f"%(Total,GPA/Total))