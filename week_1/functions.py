# python code.py to run in terminal

print('Hello world!') # string (text) func
print(10*2) # calc func
print(f'The result is {10*2}.') # f-string func

input('What is your name? ') # asking for input in the terminal

print(input('What is your name? ')) # terminal prints input after it's received

print(f"Hello, {input('What is your name? ')}!")
# f-string enables python to do things inside the string before it prints, otherwise will treat as text string

# optional arguments
print('A', 'B', 'C', sep=', ') # separate text by ,
print('A', 'B', 'C', sep=', ', end='.') # end string by .

import math # import the math module from py
print(math.floor(3.14)) # calling the floor func rounds the number down, i.e. 3
print(math.ceil(3.14)) # calling the ceil func rounds the number up, i.e. 4

from math import floor, ceil # import floor and ceil components specifically so can call directly as below
print(floor(3.14)) # or use * to import all
print(ceil(3.14))

import pandas as pd # asign alias to pandas, pandas module is in-built
