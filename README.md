# Battleship

Relive your youth with a chance to play battleship against the mighty computer.

Battleship is a game built in Python to test the users luck and/or skill in finding the computer's boat which are hidden from all radars.

![Battleship on different devices](/assets/images/amiresponive.png)

Please visit the live site [here.](https://battleship-rb.herokuapp.com/)

# UX

## Site goals

- To allow users to play a childhood game online
- To provide a challenge in the game by competing against a randomly generated player

## User stories

### New User

- A new user is interested in having fun with some time to spend online
- A new user is interested in testing out the game
- A new user is competitive and wants to beat the computer

### Returning User

- A returning user is interested in avenging a loss to the computer or improving their score
- A returning user is interested in playing on a bigger board with more boats.


# Logic flow

The chart below represents the planned goal of the site's code.

![flowchart](/assets/images/flowchart.png)

## Features

1. Start screen and board size selection.

Here the player is instructed to select the size of the board for the game. They are offered a choice from 4 to 10. Lower than 4 and the board would be too small. Greater than 10 and it would be too big. The size of the board will also determine the amount of boats on the board.

![Start screen](/assets/images/start_screen.png)

Selecting a board size outside the permitted range will incur an error message with instruction on what to pick for a valid answer.

![Number error](/assets/images/invalid_board_num.png)

Selecting a character other than a number will incur an error message.

![letter error](/assets/images/invalid_board_letter.png)

2. Instructions

After the board size is validated, a screen with the games instructions appears.

The instructions tell the player how many boats are on each board, 25% of the spaces on any board(rounded down to whole number) are occupied by a boat. 

The game is currently limited to 9 shots each, the player is informed of this on the instructions page.

![Instructions](/assets/images/instructions.png)

3. Board display at start

The initial boards are displayed before the first round. The player's board shows the players boats with the @ symbol, the player's board is referred to as the computer's target area on the screen. In between the boards are the player's and computer's scoreboards, to keep the player informed of situation.
The computer's board, referred to as the player's target area on teh screen, does not show any boats, they are hidden in the ocean of dots. 

![Board display at the start](/assets/images/board_display_start.png)

4. A player's turn

A player guesses a turn by inputting a coordindate. The first input is the row, and the second input is the column. 

If a player choose either a number not on the board or a character that is not a number, they will receive an invalid data error. They will be asked to input their guess again. 

![Invalid guess](/assets/images/invalid_guess.png)

If a player repeats a guess, their previous guess will have been stored so that the game can inform them that they already picked these coordinates and to try again.

![Repeat guess](/assets/images/repeat_guess.png)

5. Board display after a round

If the guess is validated, and the guess "hits" a boat, the "." symbol changes to an "o". if they guess doesn't hit a boat the "." changes to an "x".

When the computer guesses, the guess is validated in the background, a hit changes the "@" to an "o" and a miss changes the "." to an "x". 

If the player gets a hit, the player's score increases by one. If the computer gets a hit, the computer's score increase by one.

![Board display after a round](/assets/images/board_display_round_1.png)

The player is asked to guess again until all 9 rockets have been fired. 

6. End of the game

The games ends after 9 rounds of guesses. The scores of the computer and the player are compared and a result is determined. If the scores are equal, a draw is declared, otherwise the winner is whoever has the most points. 

The scoreboard is not repeated here as it is visible after each round. 

![final screen](/assets/images/final_screen.png)

## Technology Used

# Testing

## Bugs

## Validator

![PEP8 validator](/assets/images/pep8.png)

# Deployment

# Credit

