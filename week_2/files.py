#open a file
with open('myfile', 'w') as file: #w = write
    file.write('Line') #adds line in the file

#inspect a file
with open('myfile', 'r') as file: #r = read
    lines = file.readlines()
    print(f'The file contains {len(lines)} lines')
    for line in lines:
        print(f'Line: {line}')

LINES = ['Line']

with open('myfile', 'w') as file: #add line to file
    file.writelines(LINES)

with open('myfile', 'r') as file: #print lines
    print(file.read())

#reading a csv
import csv

with open('myfile', 'w') as file: #create CSV
    file.write('LINES')

with open('myfile', 'r') as file: #open and print
    lst = list(csv.reader(file))
    print(lst)

#DATE AND TIME FORMATTING

from datetime import datetime, date, time, timedelta #import datetime library from python

from datetime import datetime
dt = datetime(
    year = 1968, month = 6, day = 24,
    hour = 5, minute = 30, second = 0
)
print(dt) #1968-06-24 05:30:00

