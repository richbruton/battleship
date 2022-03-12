# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# build board



def board_size():
    print("Board size selection\n")
    print("Board will be a square, so entering '5' will make a 5x5 board\n")
    print("Use a board size from 4 to 10\n")
    size_str = input("Enter your board size here: \n")

    return size_str



pboard = []
cboard = []
size = int(board_size())
print(size)


for i in range(size):
    pboard.append(["."] * size )
    cboard.append(["."] * size )

# display board(computer board to be added)
    
def show_pboard(pboard):
    for row in pboard:
        print((" ").join(row))

show_pboard(pboard)


# create player and computer boats
# store player + computer boats

# player input
# verify player choice is on board(is an int and within 0, size -1) and not previously chosen
# return hit or miss, store choices in array

# computer guess from coordinates in board not already chosen from random int function
# store computers choices in array
# return hit or miss

# display hits and misses on each board

# round counter

# game winner

