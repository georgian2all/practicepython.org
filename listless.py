"""
Python 2.7

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

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

usernumber = raw_input("\nType an integer number : ")
while usernumber.isalpha():
	print "Error ! \nOnly number are allowed."
	usernumber = raw_input("\nType an integer number : ")
dlist = [item for item in alist if item < int(usernumber)]	
print "Answer 3"
print dlist
	
