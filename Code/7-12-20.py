# -*- coding: utf-8 -*-
bag_dict = dict()
found_set = set()

class Node:
    def __init__(self, color, counts, nodes):
        self.color = color
        self.counts = counts
        self.nodes = nodes
    
    def __str__(self):
        return self.color
    
    def can_contain(self, color_target):
        if self.color == color_target:
            return True
        else:
            for node in self.nodes:
                if node.can_contain(color_target):
                    return True
        return False

# Read in the input file and parse each line as data
def read_data():
    #f = open("../input/7-12-20.txt", "r")
    f = open("C:\\Users\\Steve\\Documents\\Python\\Advent2020\\Input\\7-12-20.txt", "r")
    for line in f.read().split('\n'):
        line_details = line.split("bags contain")
        bag_color = line_details[0].strip().split("bag")[0]
        bag_dict[bag_color] = []
        # bag_contains = dict()
        for bag in line_details[1].strip().split(","):
            if "no" in bag:
                bag_dict["None"] = [Node("None", dict(), [])]
            else:
                #bag_count = int(bag.strip()[:1])
                bag_label = bag.strip()[1:].split("bag")[0].strip()
                #bag_contains[bag_label] = bag_count
                bag_dict[bag_color].append(Node(bag_label, dict(), []))

def find_bag(bag_color, bag_target):
    print(bag_color, end=" ")
    if bag_color == bag_target:
        print("Found!")
        return True
    if bag_color == "None":
        print("EMPTY")
        return False
    else:
        for bag in bag_dict[bag_color]:
            return find_bag(bag.color, bag_target)
    return False

def part_one():
    count = 0
    for bag in bag_dict:
        if find_bag(bag, "shiny gold"):
            count += 1
    return count

def part_two():
    pass
    
# Compute the number of trees using different slopes
read_data()
print(part_one())
print(part_two())
