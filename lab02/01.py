
#01
time = int(input("How long have Buzz played ?: "))
hour = time//60
if time%60 > 20 : hour = hour + 1
if hour >= 5 : print(f"Total price is {(hour*900)*0.7:.0f} baht.")
elif hour == 4 : print(f"Total price is {(hour*900)*0.8:.0f} baht.")
elif 4 > hour >= 2 : print(f"Total price is {(hour*900)*0.9:.0f} baht.")
else : print(f"Total price is {(hour*900):.0f} baht.")
