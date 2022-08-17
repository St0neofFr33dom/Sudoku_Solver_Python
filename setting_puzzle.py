import string
import re

fin = open("puzzle.csv","rt")
lines= fin.readlines()
fin.close()
print(lines)
print(type(lines))
print(lines[0])
print(type(lines[0]))

puzzle = []
for row in lines:
    intermediate = row.strip(string.whitespace)
    row = intermediate.split(',')
    row = [int(i) for i in row]
    puzzle.append(row)
for line in puzzle:
    print(line)

number = puzzle[1][0]
row = 1
position = 0
if number == 0:
    possibilities = []
    while number < 9:
        number += 1
        if number in puzzle[1]:
            continue
        column = []
        for i in puzzle:
            colnum = i[0]
            column.append(colnum)
        if number in column:
            continue
        box = []
        if row <= 2:
            if position <= 2:
                for i in puzzle[0:3]:
                    for c in i[0:3]:
                        box.append(c)
        else:
            print(error)
        print(box)
        if number in box:
            continue
        else:
            possibilities.append(number)
    if len(possibilities) != 1:
        print('possible numbers =', possibilities)
        number = 0
    else:
        puzzle[1][0] = possibilities[0]
        print(puzzle)