import math
import os
import numpy as np

inputs = []

class entry():
    def __init__(self, contain, nocontain, letter, password):
        self.rule = [contain-1, nocontain-1]
        self.letter = letter
        self.password = password
    
    def process(self):
        if self.password[self.rule[0]] == self.letter:
            if self.password[self.rule[1]] == self.letter:
                return False
            else:
                return True
        else:
            if self.password[self.rule[1]] == self.letter:
                return True
            else:
                return False

def importData():
    file = open("Input2.txt", "r")

    for line in file:
        line = line.strip().split(" ")

        limits = line[0].split("-")
        letter = line[1].strip(":")
        password = line[2]

        inputs.append(entry(int(limits[0]), int(limits[1]), letter, password))

def main():
    importData()
    count = 0
    for x in inputs:
        if x.process():
            count+=1

    print(count)

if __name__ == "__main__":
    main()
