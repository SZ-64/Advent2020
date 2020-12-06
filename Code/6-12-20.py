# -*- coding: utf-8 -*-

# Read in the input file and parse each line as data
def read_data():
    f = open("../input/6-12-20.txt", "r")
    return f.read().split('\n')

def part_one():
    total = 0
    letter_set = set()
    for line in read_data():
        if line == "":
            total += len(letter_set)
            letter_set.clear()
        else:
            line_set = set(line)
            letter_set = letter_set | line_set
    return total

def part_two():
    total = 0
    new_set = True
    letter_set = set()
    for line in read_data():
        if line == "":
            total += len(letter_set)
            letter_set.clear()
            new_set = True
        else:
            line_set = set(line)
            if new_set == True:
                letter_set = line_set
                new_set = False
            else:
                letter_set = letter_set & line_set
    return total
    
# Compute the number of trees using different slopes
print(part_one())
print(part_two())
