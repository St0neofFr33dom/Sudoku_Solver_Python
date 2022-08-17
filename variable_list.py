empty_line1 = [0,0,0,0,0,0,0,0,0]
empty_line2 = [0,0,0,0,0,0,0,0,0]
empty_line3 = [0,0,0,0,0,0,0,0,0]
empty_line4 = [0,0,0,0,0,0,0,0,0]
empty_line5 = [0,0,0,0,0,0,0,0,0]
empty_line6 = [0,0,0,0,0,0,0,0,0]
empty_line7 = [0,0,0,0,0,0,0,0,0]
empty_line8 = [0,0,0,0,0,0,0,0,0]
empty_line9 = [0,0,0,0,0,0,0,0,0]
empty_box = [empty_line1,empty_line2,empty_line3,empty_line4,empty_line5,empty_line6,empty_line7,empty_line8,empty_line9]
for line in empty_box:
    print(line)
empty_box[3][2] = [3,5,7]
print(' ')
print(empty_box[3][2])
print(' ')
print(empty_box[7])
print(' ')
for line in empty_box:
    print(line)