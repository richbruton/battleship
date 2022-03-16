from random import randint

pboard = []
cboard = []
pboats = []
cboats = []
choices = []
pchoices = []
turn = 0


def board_size():
    """
    allow the player to define board size
    This will also eventually decide the number of boats
    Validation to be add for max and min board size
    """
    while True:
        print("Board size selection\n")
        print("Board is a square, so entering '5' will make a 5x5 board\n")
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
        if not data.isdigit():
            raise ValueError(
                f"You chose: {data}"
            )
        elif int(data) < 4 or int(data) > 10:
            raise ValueError(
                f"You chose: {data}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please choose a number from 4 to 10:\n")
        return False

    return True


size = int(board_size())
num_boats = int(size*size / 4)

for i in range(size):
    pboard.append(["."] * size)
    cboard.append(["."] * size)


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
    print(("==")*size)


def create_p_boats():
    """
    create player boats, store in a list and show them on the players board
    """

    while len(pboats) < num_boats:
        row = randint(0, (size - 1))
        col = randint(0, (size - 1))
        pboard[row][col] = "@"
        if [row, col] in pboats:
            continue
        else:
            pboats.append([row, col])


def create_c_boats():
    """
    create computer boats and store in a list
    """

    while len(cboats) < num_boats:
        row = randint(0, (size - 1))
        col = randint(0, (size - 1))
        if [row, col] in cboats:
            continue
        else:
            cboats.append([row, col])


def player_choice():
    """
    Input for player choice
    Verify choice is on board
    Convert . to x if a miss, . to s for a hit
    """

    while True:
        row = input("Guess your row here: \n")
        # validate_player_choice(row)
        
        col = input("Guess your column here: \n")
        # validate_player_choice(col)
        

        if validate_player_choice(row) and validate_player_choice(col):
            break

    prow = int(row)
    pcol = int(col)
    if [prow, pcol] not in pchoices:
        if cboard[prow][pcol] == "." and [prow, pcol] in cboats:
            print("player hit")
            cboard[prow][pcol] = "o"
        elif cboard[prow][pcol] == "." and [prow, pcol] not in cboats:
            print("player miss")
            cboard[prow][pcol] = "x"
        elif cboard[prow][pcol] == "o" or [prow, pcol] == "x":
            print("player, you tried there already")
    else:
        player_choice()


def validate_player_choice(data):
    """
    validate player input is an int, within the range of the board
    size, and hasnt chosen it already.
    """

    try:
        if not data.isdigit():
            raise ValueError(
                f"You chose: {data}"
            )
        elif int(data) < 0 or int(data) > (size - 1):
            raise ValueError(
                f"You chose: {data}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please choose a number from 0 to {size -1}:\n")
        return False

    return True


def computer_choice():
    """
    Input for computer choice
    Verify choice is on board
    Convert . to x if a miss, . to s for a hit
    """

    row = randint(0, (size - 1))
    col = randint(0, (size - 1))
    if [row, col] not in choices:
        if pboard[row][col] == "@" and [row, col] in pboats:
            print("computer hit")
            pboard[row][col] = "o"
            choices.append([row, col])
        elif pboard[row][col] == "." and [row, col] not in pboats:
            print("computer miss")
            pboard[row][col] = "x"
            choices.append([row, col])
    else:
        computer_choice()


def game():
    """
    while loop to run the game until the correct
    amount of turns are taken. SHowing each board and
    the score after each round
    """
    turn = 0

    while turn <= 9:
        player_choice()
        computer_choice()
        show_board(pboard)
        board_divider()
        show_board(cboard)
        turn += 1
        if turn == 9:
            end_game()


def end_game():
    print("end game")


# verify player choice is on board(is an int and within 0, size -1)
# and not previously chosen


# round counter

# game winner


def main():
    create_p_boats()
    create_c_boats()
    show_board(pboard)
    board_divider()
    show_board(cboard)
    game()


main()
