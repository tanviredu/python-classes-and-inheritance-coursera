import json
import random
import time


VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'


class WOFPlayer:
    # WOFPlayer base class

    def __init__(self, name):
        self.name = name  # name of the player
        self.prizeMoney = 0  # The amount of prize money for this player
        self.prizes = []  # The prizes this player has won so far

    def addMoney(self, amt):
        # add amt to priceMoney
        self.prizeMoney = self.prizeMoney + amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        # add prize to list prizes
        self.prizes.append(prize)

    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)


class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):

        print('''
        {} has ${}
        
        Category: {}
        Phrase:   {}
        Guessed:  {}
        '''.format(self.name, self.prizeMoney, category, obscuredPhrase, ', '.join(sorted(guessed))))

        guess = input("Guess a letter, phrase, or type 'exit' or 'pass': ")
        return guess


class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        self.name = name
        self.prizeMoney=0
        self.prizes=[]
        self.difficulty = difficulty  # semi-randomly choice whether 'good' or 'bad'

    def smartCoinFlip(self):
        random_number = random.randint(1, 10)
        if random_number > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        possible_letters = []
        impossible_letters = []
        if self.prizeMoney <250:
            for vowel in VOWELS:
                impossible_letters.append(vowel)
            impossible_letters += guessed
        else:
            impossible_letters = guessed
        for letter in LETTERS:
            if letter not in impossible_letters:
                possible_letters += letter
        return possible_letters

    def getMove(self, category, obscuredPhrase, guessed):
        possible_letters = self.getPossibleLetters(guessed)
        if len(possible_letters) == 0:
            return 'pass'
        else:
            if self.smartCoinFlip() is True:
                for letter in self.SORTED_FREQUENCIES[::-1]:
                    if letter in possible_letters:
                        return letter
            else:
                 return random.choice(possible_letters)