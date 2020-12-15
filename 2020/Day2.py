import math
import os
import numpy as np

inputs = []

class entry():
    def __init__(self, lim1, lim2, letter, password):
        self.range = [lim1, lim2]
        self.letter = letter
        self.password = password
    
    def process(self):
        count = 0
        for i in self.password:
            if i == self.letter:
                count+=1
        if self.range[0] <= count <= self.range[1]:
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
