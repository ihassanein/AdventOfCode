#################################
# Report Repair                 #
# 2 numbers that add up to 2020 #
#################################

import math
import os
import numpy as np

inputs = []

def test(numbers, target):
    indexes = {}
    for i,x in enumerate(numbers):
        indexes[x] = indexes.get(x,[])+[i]

    for i,x in enumerate(numbers):
        for j in indexes.get(target-x,[]):
            if i < j:
                return i,j

def main():
    file = open("Input1.txt", "r")

    for line in file:
        inputs.append(int(line.strip()))

    i, j = test(inputs, 2020)
    result = inputs[i] * inputs[j]
    print(result)

if __name__ == "__main__":
    main()
