#define a func
def say_hello():
	print('Hello')
say_hello() #call the func

#adding params
def say_hello(name): #name is the func parametre
	print('Hello', name)
say_hello('James') #Hello James

#returning values
def sum(x, y):
    return x + y #equation
print(sum(1, 2)) #input values, sum to 3

def grade(mark):
    if mark >= 50:
        return 'Pass'
    else:
        return 'Fail'
print(grade(73)) #pass

def divide(numerator, denominator, num_places):
	return round(numerator/denominator, num_places)
print(divide(5, 6, 3)) #5/6 to 3 decimal places = 0.833

#pass
def my_func():
    pass #must at least pass to avoid error with empty func

#give func an object
def add10(x):
    x = x + 10
    print(x) # outputs 15
