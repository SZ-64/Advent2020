# -*- coding: utf-8 -*-

# Define the reference lists
rows = [i for i in range(0,128)]
cols = [i for i in range(0,8)]

# Read in the input file and parse each line as data
def read_data():
    f = open("../input/5-12-20.txt", "r")
    return f.read().split('\n')

# Given directions, returns the seat id
def search(dirs):
    row = partition(dirs[:-3], rows, 'F')
    col = partition(dirs[-3:], cols, 'L')
    return row * 8 + col

# Recursively slice the list to find the seat
def partition(dirs, seats, part):
    if dirs == "":
        return seats[0]
    else:
        if dirs[:1] == part:
            return partition(dirs[1:], seats[:int(len(seats)/2)], part)
        else:
            return partition(dirs[1:], seats[int(len(seats)/2):], part)

def part_one():
    max_id = 0
    for seat in read_data():
        next_id = search(seat)
        if max_id < next_id:
            max_id = next_id
    return max_id

def part_two():
    seats = [False for i in range(0,1024)]
    for seat in read_data():
        seats[search(seat)] = True
    return [index for index in range(0,1024) if seats[index] == False]
    

# Compute the number of trees using different slopes
print(part_one())
print(part_two())
