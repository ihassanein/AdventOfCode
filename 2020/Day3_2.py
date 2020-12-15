import math
import os
import numpy as np

inputs = []
trees = []
slope = [
    {"right":1, "down":1},
    {"right":3, "down":1},
    {"right":5, "down":1},
    {"right":7, "down":1},
    {"right":1, "down":2},
]

def importData():
    file = open("Input3.txt", "r")

    inputs = []

    for line in file:
        line = line.strip()
        inputs.append(line)

    return np.array(inputs)

def main():
    inputs = importData()
    
    for route in slope:
        across = 0
        down = 0
        count = 0
        while down < len(inputs):
            across += route["right"]
            down += route["down"]

            if across >= len(inputs[0]):
                across = across - len(inputs[0])

            if down >= len(inputs):
                continue

            if inputs[down][across] == "#":
                count += 1
        trees.append(count)
    print(math.prod(trees))

if __name__ == "__main__":
    main()