import random

random_number = random.randint(1,10)

print("Random number between 1 to 10 is {} ".format(random_number))

## random letter generator
## list comprehension
letters = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
print (letters)

rand_letter = random.choice(letters)

print("Random Letter is : {} ".format(rand_letter))