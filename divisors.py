"""
Python 2.7

Divisors
Create a program that asks the user for a number and then prints out a list of all the divisors of that number
"""

# a function to allow to input only integer numbers 
def checknumber() :
	usernumber = raw_input("\nType a number : ")
	try:
		int(usernumber) or usernumber.isalpha()
	except ValueError:
		return checknumber()  # instead of just calling checknumber() in your try statement, you need to return it.
	else:
		return int(usernumber)
	
usernumber = checknumber()
listofnumbers = range(2,usernumber+1)
listofdivisors = [number  for number in listofnumbers if (usernumber % number == 0)]

print listofdivisors