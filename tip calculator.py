print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? :"))
people = int(input("How many people to split the bill: "))

tip_as_percent = tip / 100
total_bill = bill * (1 + tip_as_percent)
split_amount = total_bill / people

print(f"Each person should pay: ${split_amount:.2f}")
