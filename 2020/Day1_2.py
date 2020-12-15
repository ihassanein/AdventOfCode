#################################
# Report Repair                 #
# 3 numbers that add up to 2020 #
#################################

import math
import os
import numpy as np

inputs = []

def test(inputs : list):
    length = len(inputs)
    res = 0
    for i in range(length):
        res = inputs[i]
        for j in range(length):
            if i == j :
                continue
            res += inputs[j]
            for k in range(length):
                if i == k or j == k :
                    continue
                if res + inputs[k] == 2020 :
                    return i, j, k
            res -= inputs[j]  

def main():
    file = open("Input1.txt", "r")

    for line in file:
        inputs.append(int(line.strip()))

    i, j ,k =test(inputs)
    print(inputs[i], inputs[j], inputs[k])
    print(inputs[i] + inputs[j] + inputs[k])
    result = inputs[i] * inputs[j] * inputs[k]
    print(result)

if __name__ == "__main__":
    main()
