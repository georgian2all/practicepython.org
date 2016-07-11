"""
Python 2.7

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    2. Write this in one line of Python.
    3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

"""

alist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
blist = []

for item in alist:			#list on multiple code row
	if item < 5 :
		blist.append(item)
print "\nAnswer 1"
print blist

clist = [item for item in alist if item < 5 ] #list in a row
print "\nAnswer 2"
print clist


# a function to allow to input only integer numbers 
def checknumber() :
	usernumber = raw_input("\nType a number : ")
	try:
		int(usernumber) or usernumber.isalpha()
	except ValueError:
		return checknumber()  # instead of just calling checknumber() in your try statement, you need to return it.
	else:
		return int(usernumber)

number = checknumber()
dlist = set ([item for item in alist if item < number]) #second list will contain unique elemnts from first list. To get unique items, just transform it into a set (which you can transform back again into a list if required)
print "Answer 3"
print list(dlist)
	
