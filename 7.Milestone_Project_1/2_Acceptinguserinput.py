def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

# display(row1, row2, row3)

row2[1] = 'X'


display(row1, row2, row3)

position_index = int(input("Choose an index position: "))
print(row2[position_index])