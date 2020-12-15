import math
import os
import numpy as np

inputs = []

def importData():
    file = open("Input3.txt", "r")

    inputs = []

    for line in file:
        line = line.strip()
        inputs.append(line)

    return np.array(inputs)

def main():
    inputs = importData()
    count = 0
    
    across = 0
    down = 0

    while down < len(inputs):
        across += 3
        down += 1

        if across >= len(inputs[0]):
            across = across - len(inputs[0])

        if down >= len(inputs):
            continue

        if inputs[down][across] == "#":
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()