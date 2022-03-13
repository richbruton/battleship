# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


pboard = []
cboard = []


def board_size():
    """
    allow the player to define board size
    This will also eventually decide the number of boats
    Validation to be add for max and min board size
    """
    while True:
        print("Board size selection\n")
        print("Board will be a square, so entering '5' will make a 5x5 board\n")
        print("Use a board size from 4 to 10\n")

        size_str = input("Enter your board size here: \n")

        if validate_board_size(size_str):
            print(f'You have chosen a {size_str} x {size_str} board')
            break

    return size_str


def validate_board_size(data):
    """
    Validate board size to be between 4 and 10(inclusive)
    make sure board size can be converted to integer
    """

    try:
        if int(data) < 4 or int(data) > 10:
            raise ValueError(
                f"Please choose a number from 4 to 10, you chose: {data}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


size = int(board_size())

for i in range(size):
    pboard.append(["."] * size )
    cboard.append(["."] * size )

def show_board(data):
    """
    Display the player's or computer's board
    """
    for row in data:
        print((" ").join(row))

def board_divider():
    """
    Board divider to show where one board ends and the other begins
    """
    print(("- ")*size)


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

def main():
    # size = int(board_size())

    # validate_board_size(size)
    show_board(pboard)
    board_divider()
    show_board(cboard)


main()