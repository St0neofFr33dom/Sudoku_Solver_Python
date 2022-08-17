import string
import re
import copy

box= []
puzzle = []
empty_line1 = [0,0,0,0,0,0,0,0,0]
empty_line2 = [0,0,0,0,0,0,0,0,0]
empty_line3 = [0,0,0,0,0,0,0,0,0]
empty_line4 = [0,0,0,0,0,0,0,0,0]
empty_line5 = [0,0,0,0,0,0,0,0,0]
empty_line6 = [0,0,0,0,0,0,0,0,0]
empty_line7 = [0,0,0,0,0,0,0,0,0]
empty_line8 = [0,0,0,0,0,0,0,0,0]
empty_line9 = [0,0,0,0,0,0,0,0,0]
guess_box = [empty_line1,empty_line2,empty_line3,empty_line4,empty_line5,empty_line6,empty_line7,empty_line8,empty_line9]
LoRow = 0
HiRow = 0
LoCol = 0
HiCol = 0
def make_box(grid,row,col,LoRow,HiRow,LoCol,HiCol):
    if row < 3 and col < 3:
        LoRow = 0
        HiRow = 3
        LoCol = 0
        HiCol = 3
    elif row < 3 and col < 6:
        LoRow = 0
        HiRow = 3
        LoCol = 3
        HiCol = 6
    elif row < 3 and col < 9:
        LoRow = 0
        HiRow = 3
        LoCol = 6
        HiCol = 9
    elif row < 6 and col < 3:
        LoRow = 3
        HiRow = 6
        LoCol = 0
        HiCol = 3
    elif row < 6 and col < 6:
        LoRow = 3
        HiRow = 6
        LoCol = 3
        HiCol = 6
    elif row < 6 and col < 9:
        LoRow = 3
        HiRow = 6
        LoCol = 6
        HiCol = 9
    elif row < 9 and col < 3:
        LoRow = 6
        HiRow = 9
        LoCol = 0
        HiCol = 3
    elif row < 9 and col < 6:
        LoRow = 6
        HiRow = 9
        LoCol = 3
        HiCol = 6
    else:
        LoRow = 6
        HiRow = 9
        LoCol = 6
        HiCol = 9
    for i in grid[LoRow:HiRow]:
        for c in i[LoCol:HiCol]:
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
changes_2 = 0
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
            make_box(puzzle,row_off,col_off,LoRow,HiRow,LoCol,HiCol)
            if number in box: #Checks 3 by 3 box for matching numbers
                continue
            poss.append(number) #If no matching numbers, the number is a possible answer, gets added to list
        if len(poss) == 1: #If only one possible answer, gets added to the puzzle
            puzzle[row_off][col_off] = poss[0]
            #print('New number at', row_off+1, col_off+1, '=', puzzle[row_off][col_off])
            changes += 1
        elif len(poss) == 0: #Puzzle written in wrong if this happens
            print('error, no solutions at', (row_off+1) , (col_off+1))
            break
        else:
            guess_box[row_off][col_off] = poss
            #print('guess at', row_off+1, col_off+1,'=', poss)
    else:
        guess_box[row_off][col_off] = 0 #No possible value to add as there already is a value in the square
    if row_off == 8 and col_off == 8:
        if blanks == 0: #Only happens when all sqaures are filled
            break
        else:
            row_off = 0
            col_off = 0
            iteration += 1
            blanks = 0
        if changes == 0: #No changes from the 1st step
            changes_2 = False
            changes_3 = 0
            new_value = 0
            col_off = -1
            while True:
                if changes_2 == True: #This step removes the newly assigned value from the potential answers of the other sqaures in the same row, column and box
                    changes_3 += 1
                    for i in guess_box[row_off]:
                        if i != 0:
                            if new_value in i:
                                i.remove(new_value)
                    column = []
                    for j in guess_box:
                        colnum = j[col_off]
                        column.append(colnum)
                    for k in column:
                        if k != 0:
                            if new_value in k:
                                k.remove(new_value)
                    box = []
                    make_box(guess_box, row_off, col_off,LoRow,HiRow,LoCol,HiCol)
                    for l in box:
                        if l != 0:
                            if new_value in l:
                                l.remove(new_value)
                    changes_2 = False
                col_off += 1
                if row_off == 8 and col_off > 8:
                    row_off = 0
                    col_off = 0
                    #changes_3 = 1 #skips the step until fixed
                    if changes_3 == 0:
                        guess_pair = copy.deepcopy(guess_box)
                        while row_off < 9:
                            if guess_pair[row_off][col_off] != 0:
                                if len(guess_pair[row_off][col_off]) != 2:
                                    guess_pair[row_off][col_off] = 0
                            col_off += 1
                            if col_off > 8:
                                row_off += 1
                                col_off = 0
                        #for line in guess_pair:
                            #print(line)
                        #print(' ')
                        row_off = 0
                        col_off = 0
                        guess_box_2 = copy.deepcopy(guess_box)
                        while True:
                            guess = guess_pair[row_off][col_off]
                            if guess != 0:
                                count = guess_pair[row_off].count(guess)
                                if count == 2:
                                    col_off_2 = 0
                                    while col_off_2 < 9:
                                        if guess_box[row_off][col_off_2] != 0:
                                            if guess_box[row_off][col_off_2] != guess:
                                                for i in guess:
                                                    if i in guess_box[row_off][col_off_2]:
                                                        guess_box[row_off][col_off_2].remove(i)
                                                if len(guess_box[row_off][col_off_2]) == 1:
                                                    answer = guess_box[row_off][col_off_2]
                                                    puzzle[row_off][col_off_2] = answer[0]
                                                #for line in guess_box_2:
                                                    #print(line)
                                                #print(' ')
                                        col_off_2 +=1
                                    col_off_2 = 0
                                column = []
                                for j in guess_pair:
                                    colnum = j[col_off]
                                    column.append(colnum)
                                count = column.count(guess)
                                if count == 2:
                                    row_off_2 = 0
                                    while row_off_2 < 9:
                                        if guess_box[row_off_2][col_off] != 0:
                                            if guess_box[row_off_2][col_off] != guess:
                                                for i in guess:
                                                    if i in guessbox_[row_off_2][col_off]:
                                                        guess_box[row_off_2][col_off].remove(i)
                                                if len(guess_box[row_off_2][col_off]) == 1:
                                                    answer = guess_box[row_off_2][col_off]
                                                    puzzle[row_off_2][col_off] = answer[0]
                                                #for line in guess_box_2:
                                                    #print(line)
                                                #print(' ')
                                        row_off_2 += 1
                                    row_off_2 = 0
                                box = []
                                make_box(guess_pair, row_off, col_off,LoRow,HiRow,LoCol,HiCol)
                                count = box.count(guess)
                                if count == 2:
                                    row_off_2 = LoRow
                                    col_off_2 = LoCol
                                    while row_off_2 < HiRow:
                                        if guess_box[row_off_2][col_off_2] != 0:
                                            if guess_box[row_off_2][col_off_2] != guess:
                                                for i in guess:
                                                    if i in guess_box[row_off_2][col_off_2]:
                                                        guess_box[row_off_2][col_off_2].remove(i)
                                                if len(guess_box[row_off_2][col_off_2]) == 1:
                                                    answer = guess_box[row_off_2][col_off_2]
                                                    puzzle[row_off_2][col_off_2] = answer[0]
                                                #for line in guess_box_2:
                                                    #print(line)
                                                #print(' ')
                                        col_off_2 += 1
                                        if col_off_2 == HiCol:
                                            col_off_2 = LoCol
                                            row_off_2 += 1
                                    col_off_2 = 0
                                    row_off_2 = 0
                            col_off +=1
                            if col_off > 8:
                                row_off += 1
                                col_off = 0
                            if row_off > 8:
                                row_off = 0
                                col_off = 0
                                break
                        changes_3 += 1
                        continue
                    else:
                        break
                if col_off > 8:
                    row_off += 1
                    col_off = 0
                guess = guess_box[row_off][col_off]
                if guess != 0:
                    row_off_2 = 0
                    col_off_2 = 0
                    track = 0
                    for i in guess:
                        #print('checking for', i, 'in row at', row_off + 1, col_off + 1)
                        while col_off_2 < 9:
                            guess_2 = guess_box[row_off][col_off_2]
                            if guess_2 != 0:
                                if i in guess_2:
                                    track += 1
                            col_off_2 += 1
                        if track == 1: #
                            #print('row =', guess_box[row_off])
                            puzzle[row_off][col_off] = i
                            new_value = i
                            #print('New number at', row_off + 1, col_off + 1, '=', puzzle[row_off][col_off])
                            guess_box[row_off][col_off] = 0
                            changes_2 = True
                            break
                        col_off_2 = 0
                        column = []
                        track = 0
                        for j in guess_box:
                            colnum = j[col_off]
                            column.append(colnum)
                        #print('checking for', i, 'in column at', row_off + 1, col_off + 1)
                        for k in column:
                            if k != 0:
                                if i in k:
                                    track += 1
                        if track == 1:
                            #print('column =', column)
                            puzzle[row_off][col_off] = i
                            guess_box[row_off][col_off] = 0
                            new_value = i
                            #print('New number at', row_off + 1, col_off + 1, '=', puzzle[row_off][col_off])
                            changes_2 = True
                            break
                        track = 0
                        box = []
                        make_box(guess_box, row_off, col_off,LoRow,HiRow,LoCol,HiCol)
                        #print('box =', box)
                        #print('checking for', i, 'in box at', row_off+1, col_off+1)
                        for l in box:
                            if l != 0:
                                if i in l:
                                    track += 1
                        #print(i, 'appears', track, 'times')
                        if track == 1:
                            puzzle[row_off][col_off] = i
                            new_value = i
                            #print('New number at', row_off + 1, col_off + 1, '=', puzzle[row_off][col_off])
                            guess_box[row_off][col_off] = 0
                            changes_2 = True
                            break
                        track = 0

        else:
            changes = 0
            guess_box = [empty_line1,empty_line2,empty_line3,empty_line4,empty_line5,empty_line6,empty_line7,empty_line8,empty_line9]
            continue
    if col_off == 8:
        col_off = 0
        row_off += 1
    else:
        col_off += 1
    if changes_2 > 0:
        changes_2 = 0
        row_off = 0
        col_off = 0

print(' ')
for line in puzzle:
    print(line)
print(' ')
if iteration < 100:
    print('puzzle completed in', iteration, 'iterations')
else:
    print('Possible answers remaining')
    for line in guess_box:
        print(line)
    print(' ')
guess_pair = copy.deepcopy(guess_box)
row_off = 0
col_off = 0
while row_off < 9:
    if guess_pair[row_off][col_off] != 0:
        if len(guess_pair[row_off][col_off]) != 2:
            guess_pair[row_off][col_off] = 0
    col_off +=1
    if col_off > 8:
        row_off += 1
        col_off = 0
for line in guess_pair:
    print(line)

fout = open("solution.csv", 'wt') #makes new csv with solved puzzle
for line in puzzle: #needs extra steps to remove brackets being added to csv file
    print(line, file=fout)
fout.close()