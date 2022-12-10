import random
names=("arun","raju","gokul","sanjay")
random_index = random.randint(0, len(names) - 1)
random_name = names[random_index]
print(f"{random_name} is going to buy the meal today!")