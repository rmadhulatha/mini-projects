import random
friends = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
#  1 Option
random_friend = random.choice(friends)
print(f"Your random friend is: {random_friend}")

#  2 Option
random_index = random.randint(0,4)
print(f"Your random friend is: {friends[random_index]}")

#  3 Option
random.shuffle(friends)
print(f"Your random friend is: {friends[0]}")