import json
import random
import time



## get the number first

def getNumberBetween(prompt,min,max):
	userinp = input(prompt)  ## prompt is the text that is added in the prompt
	## take the input then it will run under a infinity loop
	while True:
		try:
			n = int(userinp)  ## casting to integer

			## there is a limit of input so make it
			if n < min:
				errmessage = "Must be at least {}".format(min)
			elif n>max:
				errmessage = "Must be at most {}".format(max)
			else:
				return n
		except:
			#3 if it is not a number then
			errmessage =  "{} is not a number".format(userinp)


		## it will keep asking untill it gets the number
		userinp = input("{} \n {}".format(errmessage,prompt))



# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }

## it will give you a random price or maybe give you bankrupt
## or loss
## this will be a head start and give 
def spinWheel():
	with open("wheel.json",'r') as f:
		# get the option in json
		wheel = json.loads(f.read())
		## return a random wheel
		return random.choice(wheel)







def getRandomCategoryAndPhrase():
	with open('phrases.json') as f:
		phrases = json.loads(f.read())
		## lets see how many categories there
		##print(phrases.keys())
		## we are going to choose a subject randomly
		## and need to convert to a list
		subject = list(phrases.keys())
		category = random.choice(subject);
		#print (category)
		## now get the phrase
		phrase = random.choice(phrases[category])
		#print(phrase)

		return (category,phrase.upper())
		



## obscurePhrase(phrase, guessed) returns a tuple with a random category and phrase for players to guess
# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"


## guessed will be a list of letters
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def obscurePhrase(phrase,guessed):
	## ok we give a phrase and guessed which is list of letters 
	## lets see how we make a fuzzy version
	rv = ''
	## iterate the words from the phrases
	for s in phrase:
		if(s in LETTERS) and (s not in guessed):
			## if the word that makes the phrases 
			## is in the letter (not other character)
			## and this letters in not in the guessed character
			## then
			## so iterate the phrase for word
			## and any word not in the letters will be replaced by a dashed line

			rv = rv+'_'
		else:
			## other wise
			## if in the guessed letter it will be added
			rv = rv+s
	return rv
	## so we got the obscured/fuzzy version




# Returns a string representing the current state of the game

def showBoard(category,obscurePhrase,guessed):
	return """ 
	Category : {}
	Pharese  : {}
	Guessed  : {}
	""".format(category,obscurePhrase,','.join(sorted(guessed)))



category,phrase = getRandomCategoryAndPhrase()

## create a random guessed array and fill it
guessed = []

for x in range(random.randint(10,20)):
	## we pick up some letter in differnt range
	## but minimum 10 length list
	## maxmimum 19 element list
	randomLetter = random.choice(LETTERS)
	## we will check if the letter in the guessed 
	## we dont  want duplicate
	guessed.append(randomLetter)


print("getRandomCategoryAndPhrase()\n -> ('{}', '{}')".format(category, phrase))

print("\n{}\n".format("-"*5))

print("obscurePhrase('{}', [{}])\n -> {}".format(phrase, ', '.join(["'{}'".format(c) for c in guessed]), obscurePhrase(phrase, guessed)))


print("\n{}\n".format("-"*5))

obscured_phrase = obscurePhrase(phrase, guessed)
print("showBoard('{}', '{}', [{}])\n -> {}".format(phrase, obscured_phrase, ','.join(["'{}'".format(c) for c in guessed]), showBoard(phrase, obscured_phrase, guessed)))

print("\n{}\n".format("-"*5))


num_times_to_spin = random.randint(2, 5)
print('Spinning the wheel {} times (normally this would just be done once per turn)'.format(num_times_to_spin))

for x in range(num_times_to_spin):
    print("\n{}\n".format("-"*2))
    print("spinWheel()")
    print(spinWheel())



print("\n{}\n".format("-"*5))

print("In 2 seconds, will run getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10)")

time.sleep(2)

print(getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10))

