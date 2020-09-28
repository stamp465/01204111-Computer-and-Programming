arr = ['+','-','*','/','%']
x = int(input("x: "))
o = input("Operator: ")
y = int(input("y: "))
ans = x/y
if(arr[0]==o) : print(f"{x+y}")
elif(arr[1]==o) : print(f"{x-y}")
elif(arr[2]==o) : print(f"{x*y}")
elif(arr[3]==o) : print("%.2f"%ans)
elif(arr[4]==o) : print(f"{x%y}")
else : print("Unknown Operator")