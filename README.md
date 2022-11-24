# Jumper

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

## Rules

Jumper is played according to the following rules.

- The puzzle is a secret word randomly chosen from a list.
- The player guesses a letter in the puzzle.
- If the guess is correct, the letter is revealed.
- If the guess is incorrect, a line is cut on the player's parachute.
- If the puzzle is solved the game is over.
- If the player has no more parachute the game is over.

## Requirements

The program must also meet the following requirements.

- The program must include a README file.
- The program must include class and method comments.
- The program must have at least four classes.
- The program must remain true to game play described in the overview.


## Design

The game is controlled by a Director class. The director maintains the Puzzle and Jumper classes, however leaving the implementation of each to the individual classes. Director also creates a class for the Player which will be used to get input from the player. This allows the Player class to encapsulate how it actually gets input from the user.

As a convenience, Director may create a utility class that represents terminal IO that will be used when communicating with the player and displaying the status of the word and parachute.

### Class diagram

```
Director
--------
start_game()

Puzzle
----
make_guess(): Make a guess at a letter. Return true if the letter is correct.
display_puzzle(): Display the current state of the word.
is_puzzle_solved(): Return true if the word has been guessed.

Jumper
---------
display_jumper(): Display the current state of the parachute.
cut_parachute(): Cut a line from the parachute. Return true if still some parachute left.
is_parachute(): Return true if still parachute left.

Player
------
guess_a_letter(): Player makes a guess at a letter.
```

### Sequence diagram.

1. Director initializes puzzle, jumper, and player.
    1. Puzzle reads a random word from a list.
    2. Jumper creates a full parachute state.
    3. Player initializes a new player.
2. Loop.
    1. Director displays the current puzzle and jumper status.
    2. Gets input guess from the player.
    3. Updates puzzle with the guess.
    4. Checks the puzzle to see if it has been solved.
        1. If guessed, send a won message to the player.
        2. If not guessed, send a cut parachute message to the jumper.
            1. If no parachute is left, send a game lost message to the player.
    5. If the puzzle is not solved and still parachute left, repeat the loop.
3. Game over.

## Getting Started

Make sure you have Python 3.8 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 jumper 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the jumper folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- jumper              (source code for game)
  +-- game              (specific classes)
    +-- director.py     (directs the game)
    +-- puzzle.py         (contains word puzzle)
    +-- jumper.py    (represents the parachute of the jumper.)
    +-- player.py       (represents the player.)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies

* Python 3.8

## Authors

* M. Scott Reynolds ( rey22006 at byui.edu )
