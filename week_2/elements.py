# # selecting elements
# x = [1, 2, 3]
# print(x[0]) # prints index one in the list, i.e. 1
# print(x[-1]) # prints index -1 in the list, i.e. 3
# print(x[0:3]) # prints items with indexes 0, 1, 2, i.e. 1, 2, 3
# print(x[::2]) # prints every second element

# adding elements
z = "Hello"
z = z.upper() #change to caps
y = ['a', 'b', 'c', 'd', 'e']
y.append('f') #appends f
y.insert(2, 'x') #insert x at index 2
x = ['x', 'y', 'z']
y.extend(x) #adds 2 lists together into one
y = x + y #same result
print(y)

# removing elements
x = ['a', 'b', 'c', 'd', 'e']
del x[1] #list removes index 1, b
del x[1:3] #removes index 1-2, b and c
print(x.pop(2)) #removes index 2 and returns it
x.remove('c') #removes c

# modifying elements, cannot do for tuple
x = ['a', 'b', 'c', 'd', 'e'] #list
x[0] = 'z' # assigns index 1 a new value, a becomes z

x = {1, 2, 3} #set
x.remove(3) #removes 3 and adds 4
x.add(4)

# joining elements
x = ['a', 'b', 'c', 'd', 'e']
s = ','.join(x) # joins elements of a connection into a string
print(s)

# splits list into substrings
y = 'The cat sat on the mat'
print(y.split(' '))
# ['The', 'cat', 'sat', 'on', 'the', 'mat']
