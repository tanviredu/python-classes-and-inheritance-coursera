import time
import json
import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'


class WOFPlayer:

	## this is the base class 
	## we extend it for human and computer


	## they said only the name will be inside the constructor
	## but if you set the default 
	## it does not make any diifference
	def __init__(self,name):
		self.name = name
		self.prizeMoney = 0
		self.prizes = []

	## adding method

	def addMoney(self,amt):
		
		## add the money
		self.prizeMoney = self.prizeMoney+amt

	def goBankrupt(self):
		## set the whole prize money to zero
		self.prizeMoney = 0

	def addPrize(self,prize):
		## add the prize to the list 
		## remember prizes is a list you need to append it
		self.prizes.append(prize)


	## decorator function

	def __str__(self):

		return "{} (${})".format(self.name,self.prizeMoney)


## make the class for HumanPlayer (inherited)

## .getMove(category, obscuredPhrase, guessed): Should ask the 
## user to enter a move 
## (using input()) and return whatever string they entered.


class WOFHumanPlayer(WOFPlayer):

	def getMove(self,category,obscuredPhrase,guessed):

		## first printed what is selected for you
		print("""

			{} has ${}

			Category: {}
			Phares: {}
			Guessed: {}

			""".format(self.name,self.prizeMoney,category,obscuredPhrase,','.join(sorted(guessed))));

		## remember get move take a numerical input which is the guess

		guess = input("Guess a letter, phrase, or type 'exit' or 'pass': ")
        return guess


## this is computer player ninherited class

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    ## remember the last one is the most common 
    ## first one is the rare
    ## to make a good decision we have to make a [::-1]
    def __init__(self,name,difficulty):
    	self.name = name

    	# just one more constructor
    	self.difficulty  = difficulty
    	self.prizeMoney = 0
    	self.prizes = []


    def smartCoinFlip(self):
    	random_number = random.randint(1,10)
    	if random_number > self.difficulty:
    		return True
    	else:
    		return False

   	def getPossibleLetters(self,guessed):

   		possible_letters = []
   		impossible_letters = []
   		if self.prizeMoney < 250:
   			## add the vowel to imposible list
   			for l in VOWELS:
   				impossible_letters.append(l) 
   			## now guessed word are also not in the posible letters
   			impossible_letters+=guessed
   		else:
   			## if you have money
   			## first like always guessed are always impossible
   			## so you have to do that
   			impossible_letters = guessed

   			##but the vowels are not

   		for l in LETTERS:
   			if l not in impossible_letters:
   			### in this case the impossible are the guessed letter
   			### so we dont use duplicate
   			### in the else statement there is no vowels in impossible_letters
   			### only the guesed one
   			## but id the money is low then vowels are in the impossible list
   				possible_letters+=l
   		return possible_letters

   	def getMove(sel,category,obscuredPhrase,guessed):
   		possible_letters = self.getPossibleLetters(guessed)
   		if len(possible_letters) == 0 :
   			return 'pass'
   		else:
   			if self.smartCoinFlip() is True:
   				## then we use the best

   				for l in self.SORTED_FREQUENCIES[::-1]:
   					## we reverse for the good because last one is the most used one
   					if l in possible_letters:
   						return l
   			else:
   				return random.choice(possible_letters)





