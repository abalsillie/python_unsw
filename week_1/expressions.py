message = 'hello'
print(message)
print(type(message))

hello = message # reassigning var
print(hello)

x = y = z = 100 # all assigned same value
x, y, z = 1, 2, 3 # x = 1, y = 2, z = 3

del x # removes the value of x
var = float(1) # sets the value of var to 1.0
var = str(1) # sets the value of var to string '1.0'
var = int(1.7) # sets the value of var to int '1' (rounds down)
print(var)

number = input('Number: ') # sets the value of number to the input
print(number, type(number)) # default input type is string

number = int(input('Enter a number: ')) # sets the value of number to the input and sets the input to int
print(number, type(number)) # type will be int

#NUMBERS
print(10 ** 2) # runs 10 to the power 2
print(2 ** 2 ** 3) # treated as 2**(2**3)
print(10 // 3) # 10 divided by 3 and rounded down
print(10 % 3) # asking for remainder when 10 is divided by 3, 1

x = 1
y = 1.0
print(x == y) # true
print(x != y) # doesn't equal, false
print(x is y) # false, not same var

print(round(0.1 + 0.2)) # ensure floating numbers are rounded to ensure precision

print(int('3') + float('2.0')) # converts to string and adds them // 5.0
print(abs(-5)) # absolute value // 5
print(pow(2, 4)) # 2 to the power of 4 // 16
print(round(3.567, 2)) # rounds 3.567 2 decimal places // 3.57

#STRINGS
print('Penny\'s dog is called \"Mac\".') # use backslash to print special characters

first_name = 'Alex'
last_name = 'B'
full_name = first_name + ' ' + last_name # concat full name
print(full_name)

name = 'Alex'
name += ' '
name += 'B'
print(name) # concats using augment assignment operator

print('a' * 10) #prints the string 10 times
print('fish' in 'selfishness') #true as is a 'substring'
# str1 < str2 i.e. a < b
print(len('abcde')) #prints the length of the string, i.e. 5

s = 'hello'
print(s.upper()) #prints HELLO in uppercase

#BOOLEANS
guess = int(input('Enter a number: '))
print(guess > 2 and guess < 5) #true if input conditions, otherwise false
