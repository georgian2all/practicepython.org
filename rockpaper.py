#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Python 2.7
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

"""
words = ["rock","paper","scissors"]
user1score = 0
user2score = 0

def validateinput(word):
	global words
	if word in words:
		return word
	else:
		print "Error !\n Words accepted: Rock, Paper or Scissors"
		word = raw_input("Choose rock, paper or scissors: ").lower()
		return validateinput(word)
	
def winner(word1,word2):
	global user1score
	global user2score
	if (word1 == "rock" and word2 == "scissors") or (word1 == "scissors" and word2 == "paper") or (word1 == "paper" and word2 == "rock") :
		user1score += 1
		return user1score
	elif (word2 == "rock" and word1 == "scissors") or (word2 == "scissors" and word1 == "paper") or (word2 == "paper" and word1 == "rock") :
		user2score += 1
		return user2score 
	else :
		print "It's a draw !"
		
		

def  onemoreround(user1score,user2score,fn,ln,play):
	global firstname
	global secondname
	if play == "n" :
		if user1score > user2score:
			print "The winner is: %s  | Total points: %d" % (firstname,user1score)
			print "Second place: %s   | Total points: %d" % (secondname,user2score)	
			raise SystemExit
		elif user1score < user2score:
			print "The winner is: %s  | Total points: %d" % (secondname,user2score)
			print "Second place: %s   | Total points: %d" % (firstname,user1score)
			raise SystemExit
		else:
			print "It's a draw !"	
			raise SystemExit
		
	elif play == "y":
		pass
	else:
		print "Only Y or N is accepted as input"
		play = raw_input("Play again ? (y/n): ").lower()
		return onemoreround(user1score,user2score,fn,ln,play)	
	
firstname = raw_input("First player name: ")
secondname = raw_input("Second player name: ")

while True:
	word1 = raw_input ("%s please choose rock, paper or scissors: " % firstname )
	word1 = validateinput(word1)	
	word2 = raw_input ("%s please choose rock, paper or scissors: " % secondname )
	word2 = validateinput(word2)
	winner(word1,word2)
	print "%s score: %d | %s score: %d " % (firstname,user1score,secondname,user2score)
	play = raw_input("Play again ? (y/n): ").lower() # valideaza pentru a primi ca si valoare de intrare doar Y sau n
	onemoreround(user1score,user2score,firstname,secondname,play)