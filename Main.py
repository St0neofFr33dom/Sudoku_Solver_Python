import string
import re

fin = open("puzzle.csv","rt")
lines= fin.readlines()
fin.close()

puzzle = []
for row in lines:
    intermediate = row.strip(string.whitespace)
    row = intermediate.split(',')
    row = [int(i) for i in row]
    puzzle.append(row)
for line in puzzle:
    print(line)

row_off = -1
col_off = -1
for row in puzzle:
    row_off += 1
    for position in row:
        col_off += 1
        number = position
        if number == 0:
            poss = []
            while number < 9:
                number += 1
                if number in row:
                    continue

                column = []
                for i in puzzle:
                    colnum = i[col_off]
                    column.append(colnum)
                if number in column:
                    continue

                box= []
                if row_off < 3:
                    if col_off < 3:
                        for i in puzzle[0:3]:
                            for c in i[0:3]:
                                box.append(c)
                    elif col_off < 6 and col_off >= 3:
                        for i in puzzle[0:3]:
                            for c in i[3:6]:
                                box.append(c)
                    else:
                        for i in puzzle[0:3]:
                            for c in i[6:9]:
                                box.append(c)
                elif row_off < 6 and row_off >= 3:
                    if col_off < 3:
                        for i in puzzle[0:3]:
                            for c in i[0:3]:
                                box.append(c)
                    elif col_off < 6 and col_off >= 3:
                        for i in puzzle[0:3]:
                            for c in i[3:6]:
                                box.append(c)
                    else:
                        for i in puzzle[0:3]:
                            for c in i[6:9]:
                                box.append(c)
                else:
                    if col_off < 3:
                        for i in puzzle[0:3]:
                            for c in i[0:3]:
                                box.append(c)
                    elif col_off < 6 and col_off >= 3:
                        for i in puzzle[0:3]:
                            for c in i[3:6]:
                                box.append(c)
                    else:
                        for i in puzzle[0:3]:
                            for c in i[6:9]:
                                box.append(c)
                if number in box:
                    continue
                poss.append(number)
            if len(poss) != 1:
                print('possible numbers =', poss)
                number = 0
            else:
                puzzle[row_off][col_off] = poss[0]

print(puzzle)
