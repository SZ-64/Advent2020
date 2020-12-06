# -*- coding: utf-8 -*-

def sort_nums():
    f = open("../input/1-12-20.txt", "r")
    nums = f.read().split('\n')
    return sorted([int(num) for num in nums])

def part_one():
    nums = sort_nums()
    for bot in range(0, len(nums) - 1, 1):
        for top in range(len(nums) - 1, bot, -1):
            if nums[bot] + nums[top] == 2020:
                return nums[bot] * nums[top]
            
def part_two():
    nums = sort_nums()
    for bot in range(0, len(nums) - 1, 1):
        for mid in range(bot + 1, len(nums) - 1, 1):
            for top in range(len(nums) - 1, -1, -1):
                if nums[bot] + nums[mid] + nums[top] == 2020:
                    return nums[bot] * nums[mid] * nums[top]
            
print(part_one())
print(part_two())
