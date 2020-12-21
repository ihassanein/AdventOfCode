seats = []
seatIDs = []
rows = []
columns = []

def importData():
    file = open("Input5.txt", "r")
    for line in file:
        seats.append(line.strip())

def main():
    importData()
    for seat in seats:
        row = list(range(128))
        column = list(range(8))
        for i in range(len(seat)):
            if i <= len(seat[:-3]):
                if seat[i] == "F":
                    del row[len(row)//2:]
                else:
                    del row[:len(row)//2]
                rows.append(row)
            else:
                if seat[i] == "L":
                    del column[len(column)//2:]
                else:
                    del column[:len(column)//2]
                columns.append(column)
            seatIDs.append(row[0]*8 + column[0])
    print(max(seatIDs))

if __name__ == "__main__":
    main()