print("Welcome to Treasure Island.") 
print("Your mission is to find the trasure.")
choice1 = input("Your at cross road, where do you want to go? ")
if choice1 == 'right':
    print("Fell into a hole.")
    print("Game Over")
else:
    choice2 = input("You have came to a lake, there is an island in the middle of the lake. What you will do wait or swim.")
    if choice2 == 'wait':
        print("Attacked by dark monster")
    else:
        choice3 = input("After swimming you entered into the island. there are tree doors infront of you which one will you choose red, yellow, blue")
        if choise3 == 'Red':
            print("Burned by fire Game Over.")
        elif choise3 == 'Blue':
            print("Killed by pirates Game Over.")
        else:
            print("You found the treasure.")
