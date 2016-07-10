"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
from datetime import date
today = str(date.today())
today = int(today[0:4])

def calculateyear():
	global today
	age = raw_input("Your age today : ")	
	while age.isalpha():
		print "Error!\nPlease input an integer value! \n"
		age = raw_input("Your age today : ")
		
	agetobeyearsold  = raw_input("Years old: ")	
	while agetobeyearsold.isalpha():
		print "Error!\nPlease input an integer value! \n"
		agetobeyearsold  = raw_input("Years old: ")
	
	ouryear = today + (int(agetobeyearsold)-int(age))
	
	return str(ouryear)
	

print "You will turn 100 years old in " + calculateyear()
