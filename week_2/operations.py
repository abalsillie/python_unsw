evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

#returns the union of these 2 sets, in numerical order, removing duplicates
print(evens | primes)
print(evens.union(primes)) #or vice versa

#returns the intersection of these 2 sets, i.e. 2
print(evens & primes)
print(evens.intersection(primes)) #or vice versa

#returns the difference of these 2 sets
print(evens - primes) # 4, 6, 8 - vice versa would return 3, 5, 7
print(evens.difference(primes))

#returns the difference of BOTH of these 2 sets
print(evens.symmetric_difference(primes))

#returns true if no elements are in common
print(evens.isdisjoint(primes))

#checks if one set is a subset of another
A = {2, 3}
B = {2, 3, 6, 7}
print(A.issubset(B)) #true
print(A <= B) #true

#checks if one set is a superset of another
print(B.issuperset(A)) #true
print(B >= A) #true

#looping
vowels = ['a', 'e', 'i', 'o', 'u']
for v in vowels: #v represents single index in a list, can also do for tuples, sets and dictionaries
    print(v) #prints a e i o u, sets are not ordered so could be returned in any order

#returns the index number of a value
for index in enumerate(vowels):
	print(index) #prints index numbers 0-4

for i, value in enumerate(vowels):
	print(i, value) #also prints value
#
print('before o:')
for v in vowels:
    if v == 'o':
        break #stop when you get to o, i.e. a, e, i

print('except o:')
for v in vowels:
    if v == 'o':
        continue #skips o and then keeps going, i.e. a, e, i, u

#dictionary example
scores = {'Alice': 0, 'Bob': 1, 'Eve': 2, 'Mallory': 3}
for key, value in scores.items():
	print(f'{key} scored {value}') #returns Alice scored 0, etc

#to loop through just values
for x in scores.values(): #returns 0, 1, 2, 3
	print(x)

#nested loops
lists = [[1, 2, 3], [3, 4, 5], [5, 6, 7]] #list of lists
total = 0
for lst in lists:
    for num in lst: #number inside sublist, nested loop
        total += num #sum total = 36

#list comprehensions
words = ['the', 'quick', 'brown', 'fox']
lengths = [len(word) for word in words] # returns 3, 5, 5, 3

nums = [2, 12]
nums = [x for x in nums if x >= 10] #if condition, returns 12

#set comprehensions: are unique, so will not return same number twice
unique_lengths = {len(word) for word in words}

#RANGE
#range function will return a range, not a list, unless converted to list
for i in range(10): #start is assumed to be zero
	print(i) #prints numbers 0 - 9

for i in range(3, 10): #count from 3 to 9

for i in range(0, 10, 2): #count from 0 to 10 but count every second number, 0, 2, 4, 6, 8

vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(vowels)):
    print(i, vowels[i]) #returns 0 a, etc
