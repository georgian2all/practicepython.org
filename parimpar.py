"""
Python 2.7
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


"""

def oddeven(first,second):
	first = int(first)
	second = int(second)
	if first % 2 != 0 :
		print str(first) + " is an odd number."
	elif first % 4 ==0 :
		print str(first) + " is a multiple of 4"	
	else:
		print str(first) + " is an even number."
		
	if (first % 4 ==0) and (first % 2 == 0) :
		print str(first) + " is an even number."
		
	if (first % second == 0):
		print str(first) + " divides evenly by " + str(second)
	else:
		print str(first) + " doesn't divides evenly by " + str(second)
		

first = raw_input("First number : ")	
while first.isalpha():
	print "Error!\nPlease input an integer value! \n"
	first = raw_input("First number : ")
		
second  = raw_input("Second number: ")	
while second.isalpha():
	print "Error!\nPlease input an integer value! \n"
	second  = raw_input("Second number: ")
	

	
oddeven(first,second)