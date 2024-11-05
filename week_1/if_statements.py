number = int(input('What is your favourite number? '))
if number == 42:
    print('YAY!') #if meets conditions MUST BE INDENTED 
elif number == 21: #else if
    print('Close!')
else: #else
    print('Oh no!')

if 2 > 1 and 2 < 3:
    print('The condition is true')

x = 24
even = "even" if x % 2 == 0 else "odd" #remainder = 0, TERNARY EXPRESSION
print(even)

#WHILE
n = 1
while n <= 10: #loops through until n gets to 10
    #if n % 2 == 0: would only loop even numbers
    print(n)
    n = n + 1

i = 0
while i < 10:
    i += 1
    if i == 5:
	    break #code stops when i gets to 5
    print(i)