print("Welcome to Python Pizza Deliveries!!")
size = input("What size pizza wouls like? S, M, L: ")
pepperoni = input("Would you like pepperoni on your pizza?: ")
cheese = input("Would you like to have extra cheese?: ")

bill = 0
if size == "s":
    bill+= 15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else:
    print("You typed the wrong input.")
if pepperoni == "Y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill+=1
print(f"Your final bill is {bill}")