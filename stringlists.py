#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
Discussion

Concepts for this week:

    List indexing
    Strings are lists

"""

ourstring = raw_input('Type your string: ')

if ourstring == ourstring[::-1]:
    print "Your string is a palindrome"
else:
	print "Reversed string: ", ourstring[::-1]
	print "Your string is not a palindrome"
