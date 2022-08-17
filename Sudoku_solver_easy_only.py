import string
import re

box= []
puzzle = []
intermediate = [[0]*9]*9

def make_box(LowRow,HiRow,LowCol,HiCol):
    for i in puzzle[LowRow:HiRow]:
        for c in i[LowCol:HiCol]:
            box.append(c)

fin = open("puzzle.csv","rt") #right now the sudoku needs to be put in csv format, blanks are put down as 0
lines= fin.readlines()
fin.close()

for row in lines:
    intermediate = row.strip(string.whitespace) #parsing from csv is weird, random spaces can pop up
    row = intermediate.split(',') #create the arrays seperating values via the commas
    row = [int(i) for i in row]
    puzzle.append(row) #puzzle made of 9 lists (rows), each list has 9 values
for line in puzzle:
    print(line)

iteration = 0
row_off = 0
col_off = 0 #column and row offsets
blanks = 0
changes = 0
while True:
    if iteration >= 100: #very simple method only works for easy puzzles, next step to be added for harder puzzles
        print('puzzle is too difficult for this method')
        break
    number = puzzle[row_off][col_off]
    if number == 0: #i.e. if the square doesn't have a number assigned yet
        blanks +=1
        poss = []
        while number < 9:
            number += 1
            if number in puzzle[row_off]: #Checks row for matching number
                continue
            column = []
            for i in puzzle:
                colnum = i[col_off]
                column.append(colnum)
            if number in column: #Checks column for matching number
                continue
            box= []
            if row_off < 3 and col_off < 3:
                make_box(0,3,0,3)
            elif row_off < 3 and col_off < 6:
                make_box(0,3,3,6)
            elif row_off < 3:
                make_box(0,3,6,9)
            elif row_off < 6 and col_off < 3:
                make_box(3,6,0,3)
            elif row_off < 6 and col_off < 6:
                make_box(3,6,3,6)
            elif row_off < 6:
                make_box(3,6,6,9)
            elif col_off < 3:
                make_box(6,9,0,3)
            elif col_off < 6:
                make_box(6,9,3,6)
            else:
                make_box(6,9,6,9)
            if number in box: #Checks 3 by 3 box for matching numbers
                continue
            poss.append(number) #If no matching numbers, the number is a possible answer, gets added to list
        if len(poss) == 1: #If only one possible answer, gets added to the puzzle
            puzzle[row_off][col_off] = poss[0]
            changes += 1
        elif len(poss) == 0: #Puzzle written in wrong if this happens
            print('error, no solutions at', (row_off+1) , (col_off+1))
            break
        else:
            intermediate[row_off][col_off] = poss
    if row_off == 8 and col_off == 8:
        if blanks == 0: #Only happens when all sqaures are filled
            break
        else:
            row_off = 0
            col_off = 0
            iteration += 1
            blanks = 0
            #for line in puzzle:
                #print(line)
            #print(' ')
        if changes == 0:
            for line in intermediate:
                print(line)
                break
        else:
            changes = 0
            continue
    if col_off == 8:
        col_off = 0
        row_off += 1
    else:
        col_off += 1




fout = open("solution.csv", 'wt') #makes new csv with solved puzzle
for line in puzzle: #needs extra steps to remove brackets being added to csv file
    print(line, file=fout)
fout.close()