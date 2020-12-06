# -*- coding: utf-8 -*-

# Read in the input file and parse each line as a row of trees
def read_forest():
    f = open("../input/3-12-20.txt", "r")
    return f.read().split('\n')

# Count the trees down a slope of -1/3
def part_one():
    counts = [0,0] # [0] = col, [1] = trees
    for row in read_forest():
        if row[counts[0]] == '#':
            counts[1] += 1
        counts[0] = (counts[0] + 3) % len(row)
    return counts[1]
        
# Counts the tress given the supplied rises and runs
def part_two(rise, run):
    counts = [0,0,0] # [0] = rise, [1] = run, [2] = tree
    for row in read_forest():
        if counts[0] > 1:
            counts[0] -= 1
        else:
            if row[counts[1]] == '#':
                counts[2] += 1
            counts[0] = rise
            counts[1] = (counts[1] + run) % len(row)
    return counts[2]

# Compute the number of trees using different slopes
print(part_two(1, 1))
print(part_two(1, 3)) # <-- Part one solution
print(part_two(1, 5))
print(part_two(1, 7))
print(part_two(2, 1))
