import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"Pssst, The solution is : {chosen_word}.")

guess = input("Guess a Letter : ")

display = []

for letter in chosen_word:
    display += "_"
print(display)
    	