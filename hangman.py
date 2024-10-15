
import random

game_words=["mango","apple","banana","orange","strawberry","pineapple","cantaloupe","blueberry","grape","guava"]

chosen_word = random.choice(game_words)

print(chosen_word)
word_dashes = "_"*(len(chosen_word))

print("Guess the word! HINT! name is word is a name of a fruit: \n {}".format(word_dashes))



allowed_number_of_tries = len(chosen_word) + 2
number_of_tries = 0
user_result = list(word_dashes)
while number_of_tries < allowed_number_of_tries:
    user_guess = input("Enter a letter to guess:")

    for i,c in enumerate(chosen_word):
        if c == user_guess:
            user_result[i] = c
    if "_" not in user_result:
        print("Hooray!! You won \n {}".format("".join(user_result)))
        break
    print("".join(user_result))
    number_of_tries = number_of_tries + 1

    if number_of_tries == allowed_number_of_tries:
        print("Sorry!! You lost! Word is {}".format(chosen_word))
    







