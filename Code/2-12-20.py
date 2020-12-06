# -*- coding: utf-8 -*-

def read_list():
    f = open("../input/2-12-20.txt", "r")
    items = f.read().split('\n')
    return [item.split(' ') for item in items]

def part_one():
    result = 0
    matrix = read_list()
    for item in matrix:
        min_max = item[0].split('-')
        min_num = min_max[0]
        max_num = min_max[1]
        letter = item[1][:1]
        count = item[2].count(letter)
        if (count >= int(min_num) and count <= int(max_num)):
            result += 1
    return result
            
def part_two():
    result = 0
    matrix = read_list()
    for item in matrix:
        min_max = item[0].split('-')
        min_pos = min_max[0]
        max_pos = min_max[1]
        letter = item[1][:1]
        pos_one = item[2][int(min_pos) - 1]
        pos_two = item[2][int(max_pos) - 1]
        if ((pos_one == letter) ^ (pos_two == letter)):
            result += 1
    return result
            
print(part_one())
print(part_two())
