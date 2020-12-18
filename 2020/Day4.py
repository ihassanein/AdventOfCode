import math
import os
import numpy as np

passports = []

class passport():
    def __init__(self):
        self.fields = {
            "byr":None,
            "iyr":None,
            "eyr":None,
            "hgt":None,
            "hcl":None,
            "ecl":None,
            "pid":None,
        }
    def verify(self):
        print(self.fields)
        for key, value in self.fields.items():
            if value == None:
                return False
        return True

def importData():
    file = open("Input4.txt", "r")

    index = 0
    passports.append(passport())

    for line in file:
        if line != '\n':
            creds = line.strip().split(" ")
            for entry in creds:
                entry = entry.split(":")
                key = entry[0]
                data = entry[1]

                if key in passports[index].fields.keys():
                    passports[index].fields[key] = data

        else:
            index += 1
            passports.append(passport())

def main():
    importData()

    count = 0

    for passport in passports:
        if passport.verify():
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()