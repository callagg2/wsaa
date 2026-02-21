#reading in data from a csv file
# author: gerry callaghan

import csv

FILENAME = "data.csv"
#DATADIR = "where did you put it"

'''
#with open(DATADIR + FILENAME, "r") as csvfile:
with open(FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line)

'''
'''
with open(FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        print(f"the value of line is: {line} and linecount is {linecount}")
        print(f"the value not linecount is: {not linecount}")
        if  not linecount: # first row is header, the value of header is zero, so "not zero" is true
            print(f"{line}\n----------")
        else: # all subsequent rows are data
            print(line)
        linecount += 1
    print(f"\nThere were {linecount} lines in the file.")

'''

with open (FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row ie header row
            print (f"header is {line}\n----------")
        else: # all subsequent rows
            total += line[1] # why 1
            linecount += 1

    print (f"average is {total/(linecount-1)}") # why -1 ?


