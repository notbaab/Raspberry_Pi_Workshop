# Python syntax and crash course

# First here is an assignment to a varible
x = 2

# one of the unique things about python is sequences. Sequences are a lot of 
# different values in one varible. They come in three flavors list, tuples and 
# dictionaries.

# Lists are defined with brackets []. Below in an empty list
a_list = []

# you can also add stuff to the list in the assignment (what's assignment?). Do 
# so by adding a value and a comma (,) after
a_list = [1,2,3]

# to modify a list value you can use what is called the index. In the below code
# the first value, which was 1, is now five. 
a_list[0] = 5
# The list looks like [5,2,3] now

# one very useful thing in lists is the append function. You can call append on 
# a list to add a value at the very end of the list. This is very useful, if 
# anyone took java, remember having to preallocated the size of arrays?
a_list.append(10)
# The list looks like [5,2,3, 10] now

# a tuple is very similar to lists but use parentheses () instead. 
a_tuple = ()
a_tuple = (1,2,3)
# you CANNOT assign values in a tuple or use the append method. 

# Use tuples when you know all the values around of time, use list when you will
# be modifying values

# A dictionary is a very powerful sequence. It is like a list however you 
# don't need to use a number as an index, instead you use what is called a key. 
# a key is just a string

# initialize with curly braces {}
a_dict = {}

# when you make a dictionary, you can assign values in the initialization.
a_dict = {'key':'value'}

# access the values by using the key as the "index" in brackets. Below it will 
# print the string value
print a_dict['key']

# Assignment works the same way on a dict as it does a list. Below changes the 
# value at key to the number (int) 0
a_dict['key'] = 0

# to add another value to the dict you don't need a fancy append function, just 
# use the index as if it was already there
a_dict['different_key'] = "I'm a string!!"


# an if statment is followed by a colon!! As with elif, for statements and while
# loops. 
if x < 4 and x > 0:
	print "x is so small\n"
elif x>4 or x<0:
	print "x is big, yo!\n"
else
	print "how did you get here?"


# A four loop is only used on sequences. The first time the for loop is run it
# will print one. The second time it will print 2.=
for x in [1,2]:
	print x

while x<4:
	x += 1 # this is how you added on to a value!
	print x

























