# -*- coding: utf-8 -*-

# Define the Credential object for storage and validation
class Credential:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
    
    def is_valid(self):
        return \
            self.byr != "" and self.iyr != "" and \
            self.eyr != "" and self.hgt != "" and \
            self.hcl != "" and self.ecl != "" and \
            self.pid != ""
    
    def is_extra_valid(self):
        return \
            self._is_valid_byr() and \
            self._is_valid_iyr() and \
            self._is_valid_eyr() and \
            self._is_valid_hgt() and \
            self._is_valid_hcl() and \
            self._is_valid_ecl() and \
            self._is_valid_pid()
    
    def _is_valid_byr(self):
        return \
            self.byr != "" and \
            int(self.byr) >= 1920 and \
            int(self.byr) <= 2002
            
    def _is_valid_iyr(self):
        return \
            self.iyr != "" and \
            int(self.iyr) >= 2010 and \
            int(self.iyr) <= 2020
    
    def _is_valid_eyr(self):
        return \
            self.eyr != "" and \
            int(self.eyr) >= 2020 and \
            int(self.eyr) <= 2030
    
    def _is_valid_hgt(self):
        return \
            self.hgt != "" and \
            ((self.hgt[-2:] == "cm" and \
             int(self.hgt[:-2]) >= 150 and \
             int(self.hgt[:-2]) <= 193) or 
            (self.hgt[-2:] == "in" and \
             int(self.hgt[:-2]) >= 59 and \
             int(self.hgt[:-2]) <= 76))
            
    def _is_valid_hcl(self):
        return \
            self.hcl != "" and \
            self.hcl[0:1] == "#" and \
            len(self.hcl[1:]) == 6
    
    def _is_valid_ecl(self):
        return \
            self.ecl != "" and \
            (self.ecl == "amb" or \
             self.ecl == "blu" or \
             self.ecl == "brn" or \
             self.ecl == "gry" or \
             self.ecl == "grn" or \
             self.ecl == "hzl" or \
             self.ecl == "oth")
    
    def _is_valid_pid(self):
        return \
            self.pid != "" and len(self.pid) == 9

# Read in the input file and parse each line as data
def read_data():
    data = []
    f = open("../input/4-12-20.txt", "r")
    lines = f.read().split('\n')
    for line in lines:
        cur_cred = {"byr":"", "iyr":"",
                    "eyr":"", "hgt":"",
                    "hcl":"", "ecl":"",
                    "pid":"", "cid":""}
        for token in line.split(' '):
            elems = token.split(':')
            if len(elems) > 1:
                cur_cred[elems[0]] = elems[1]
        data.append(Credential(cur_cred["byr"], cur_cred["iyr"],
                           cur_cred["eyr"], cur_cred["hgt"],
                           cur_cred["hcl"], cur_cred["ecl"],
                           cur_cred["pid"], cur_cred["cid"]))
    return data

# Scans all credentials and counts the valid ones
def part_one():
    count = 0
    for cred in read_data():
        if cred.is_valid():
            count += 1
    return count
        
# Counts the tress given the supplied rises and runs
def part_two():
    data = read_data()
    count = 0
    for cred in data:
        if cred.is_extra_valid():
            count += 1
    return count

# Compute the number of trees using different slopes
print(part_one())
print(part_two())
