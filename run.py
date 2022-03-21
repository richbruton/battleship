from random import randint

pboard = []
cboard = []
pboats = []
cboats = []
choices = []
pchoices = []


def board_size():
    """
    Allow the player to define board size
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


def game_rules():
    """
    Display the number of boats in the game
    Show the rules for the game
    Explain the cooridnates
    """
    boats = sum(x.count('@') for x in pboard)
    print(f"There will be {boats} boats on each board")
    print("You will have 9 attempts to hit as many boats as possible.\n")
    print("The computer also has 9 attempts.\n")
    print("If you strike all their boats early in the game,")
    print("the computer can still strike your boats later in the game.")
    print("The winner will be the team that has hit the most boats")
    print("at the end of the game.\n")
    print("The coordinates for each corner of the board are:\n")
    print("Top left hand corner: (0,0)")
    print(f'Top right hand corner: (0,{size -1})')
    print(f'Bottom left hand corner: ({size -1},0)')
    print(f'Bottom right hand corner: ({size -1},{size -1})')
    print("'.' is an unhit square, 'x' is where a missile landed but missed,")
    print("'o' is a ship that has been hit, '@' is the player's ships.")
    print("The computer's ships dont turn up on our radar, find them!")
    print("Good luck!\n")


def validate_board_size(data):
    """
    Validate board size to be between 4 and 10(inclusive)
    Make sure board size can be converted to integer
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
    pscore = sum(x.count('o') for x in cboard)
    cscore = sum(x.count('o') for x in pboard)

    print("^^Computer target area")
    print(f"Player score: {pscore}")
    print(f"Computer score: {cscore}")
    print("vv Player target area")


def create_boats(data, data1):
    """
    Create boats, store in a list and show them on the board
    """

    while len(data) < num_boats:
        row = randint(0, (size - 1))
        col = randint(0, (size - 1))
        if data1 == pboard:
            data1[row][col] = "@"
        else:
            pass
        if [row, col] in pboats:
            continue
        else:
            data.append([row, col])


def player_choice():
    """
    Input for player choice
    Verify choice is on board
    Convert . to x if a miss, . to s for a hit
    """

    while True:
        row = input("Guess your row here: \n")
        col = input("Guess your column here: \n")

        if validate_player_choice(row) and validate_player_choice(col):
            break

    prow = int(row)
    pcol = int(col)
    if [prow, pcol] not in pchoices:
        if cboard[prow][pcol] == "." and [prow, pcol] in cboats:
            cboard[prow][pcol] = "o"
            pchoices.append([prow, pcol])
        elif cboard[prow][pcol] == "." and [prow, pcol] not in cboats:
            cboard[prow][pcol] = "x"
            pchoices.append([prow, pcol])
    elif [prow, pcol] in pchoices:
        print(f"You have already guessed {prow},{pcol}. Try again, try better")
        player_choice()
    else:
        player_choice()


def validate_player_choice(data):
    """
    Validate player input is an int, within the range of the board
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
        print(f"Invalid data:{e}. Please choose a number from 0 - {size -1}\n")
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
            pboard[row][col] = "o"
            choices.append([row, col])
        elif pboard[row][col] == "." and [row, col] not in pboats:
            pboard[row][col] = "x"
            choices.append([row, col])
    else:
        computer_choice()


def game():
    """
    While loop to run the game until the correct
    amount of turns are taken. SHowing each board and
    the score after each round
    """
    turn = 1

    while turn < 10:
        print(f'Round: {turn}')

        player_choice()
        computer_choice()
        show_board(pboard)
        board_divider()
        show_board(cboard)
        turn += 1
        if turn == 10:
            end_game()
            break


def end_game():
    """
    Determine and print result of game
    """
    pscore = sum(x.count('o') for x in cboard)
    cscore = sum(x.count('o') for x in pboard)

    if pscore == cscore:
        print("A draw")
    elif pscore > cscore:
        print("Player wins")
    elif pscore < cscore:
        print("Computer wins")


def main():
    """
    Function to call all other functions
    """
    create_boats(pboats, pboard)
    create_boats(cboats, cboard)
    game_rules()
    show_board(pboard)
    board_divider()
    show_board(cboard)
    game()


main()
