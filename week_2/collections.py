# Types of collections:
# Lists (ordered collection of objects)
x = [] # empty list
y = [2, 4, 6, 8]
print(y)

# Tuples (immutable/ uneditable list)
y = (2, 4, 6, 8)
(x, y) = (1, 2) # x = 1, y = 2

# Sets (unordered list of unique objects)
x = {2, 4, 6, 8}

# Dictionaries (ordered collection of key-value pairs)
x = {1: 'cat', 2: 'dog', 3: 'mouse'}
y = {True: 1, False: 0}

# Collections of collections
# list of lists
x = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
print(x)

# set of tuples
x = {(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')}
print(x)

# list(), tuple(), set(), and dict()
# turning a tuple into a list e.g.
x = list((1, 2, 3))
print(x)

# Creating a set from a list can be a good way to remove duplicate items from the list
x = [1, 2, 2, 1, 3, 3, 2, 3, 1]
x = set(x)
print(x)

# sort a list
x.sort()
x.sort(reverse=True) # in reverse
x.reverse() # sorts the list itself in reverse order, not in numerical order
x.sort(key=len) # sorts list in length, e.g...
x = ['dog', 'chicken', 'mouse', 'horse', 'goat', 'donkey']
print(x)

# checking a list
print(len([1, 2, 3])) # length of a list, i.e. 3
print(1 in [1, 2, 3]) # check existance of item in the list, i.e. True
x = [1, 2, 3]
print(x.index(1)) # checks index of that number, i.e. 0
print(x.count(1)) # counts number of time 1 occurs in the list, i.e. 1
print(min([1, 2, 3])) # prints the smallest value, i.e. 1
print(sum([1, 2, 3])) # sums the list, i.e. 6
