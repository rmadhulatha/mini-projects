print("Welcome to the rollercoaster!!")
height = int(input("Enter your height in cm : "))

if height>=150:
    print("You can ride the rollercoaster.")
    age = int(input("Enter your age: "))
    if age<=12:
        bill = 5
        print(" Child ticket is $5")
    elif age<=18:
        bill = 7
        print("Youth ticket is &7")
    else:
        bill = 10
        print("Adult ticket is $10")
    photos = input("Would you like to take some photos? if yes type 'y' and type 'n' for no: ")
    if photos=="y":
        bill += 3
        print(f"Your total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")
else:
    print("Sorry you are not eligible to ride rollercoaster")