# -*- coding: utf-8 -*-
"""
Python 2.7
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Extras:
2. Randomly generate two lists to test this
3. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
Simple solution:
print set(a).intersection(set(b))
"""
import random

firstlist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
secondlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#first and third problem
commonelements = list(set([item for item in firstlist if item in secondlist] ))
print "\nThe answer to the first requirement"
print "First list: ", firstlist
print "Second list: ", secondlist
print "Common elements: ", commonelements

#second problem
firstlist = []
secondlist = []
x = random.randint(1,10) #generate a random number for length of first list. random list length
y = random.randint(1,10) #generate a random number for length of second list. random list length

for number in range(x):
	firstlist.append(random.randint(1, x)) #append random numbers to list
	
for number in range(y):
	secondlist.append(random.randint(1, y)) #append random numbers to list

commonelements = [item for item in firstlist if item in secondlist] 
commonelements = list(set(commonelements))
print "\nThe answer to the second requirement"
print "First random list: ", firstlist
print "Second random list: ", secondlist
print "Common elements: ", commonelements

