import random
print("Enter minimum number of Range: ")

min_num = int(input())

print("Enter maximum number of Rage:")

max_num = int(input())

print(min_num + max_num)

guess_number = random.randrange(min_num,max_num,1)

print("Guess the Random Number")

number_of_tries = 0


while number_of_tries < 5:

    my_guess_number = int(input())

    number_of_tries = number_of_tries + 1

    if my_guess_number == guess_number:
        print("Hooray!! You guessed right on try "+str(number_of_tries))
        exit(0)
    if my_guess_number < guess_number:
        print("You guessed to Small")
    elif my_guess_number > guess_number:
        print("You guessed to High")

    
        
print("You failed after {0} tries!! Number is {1}".format(number_of_tries,guess_number))       
    

    