import math
import os
import numpy as np
import string

passports = []
colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

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
        for key, value in self.fields.items():
            if value == None:
                print("False because None field")
                return False

            else:
                if key == "byr":
                    value = int(value)
                    if 1920 > value or 2002 < value:
                        print("False because byr field")
                        return False
                
                if key == "iyr":
                    value = int(value)
                    if 2010 > value or 2020 < value:
                        print("False because iyr field")
                        return False
                
                if key == "eyr":
                    value = int(value)
                    if 2020 > value or 2030 < value:
                        print("False because eyr field")
                        return False
                
                if key == "hgt":
                    try:
                        number = int(value[:-2])
                    except ValueError:
                        print("False because hgt field")
                        return False

                    unit = value[-2:]
                    
                    if unit == "cm":
                        if 150 > number or 193 < number:
                            print("False because hgt field")
                            return False
                    elif unit == "in":
                        if 59 > number or 76 < number:
                            print("False because hgt field")
                            return False
                    else:
                        print("False because no unit field")
                        return False
                
                if key == "hcl":
                    if value[0] == "#":
                        if not all(char in string.hexdigits for char in value[1:]):
                            return False
                    else:
                        return False

                if key == "ecl":
                    if value not in colours:
                        print("False because ecl field")
                        return False
                
                if key == "pid":
                    if len(value) != 9:
                        print("False because pid field")
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
            print (count)
    
    print(count)

if __name__ == "__main__":
    main()