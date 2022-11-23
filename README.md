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
### Class diagram

```
Puzzle
--------
_jumper: Current word and status of jumper
_player: Player interface
start_game()

Jumper
------
_word: Current word.
_parachute: Parachute state.
make_guess(): Check letter to see if it is a match. 
display_status(): Display the current game state.
is_won(): Return true if game has been wone.
is_lost(): Return true if game has been lost.

Player
------
new_player(): Initialize player. 
get_guess(): Player makes a guess at a letter.

Word
----
_current_word
_current_state
create_word(): Create a new word.
make_guess(): Make a guess at a letter
word_guessed(): Return true if word has been guessed.

Parachute
---------
_parachute_list
create_parachute(): Initialize parachute.
cut_parachute(): Cut a line from parachute. Return true if not lost.
```

### Sequence diagram.
1. Puzzle initializes jumper and player.
    1. Jumper initializes Word and Parachute.
        1. Word reads random word from a list.
        2. Parachute creates full parachute state.
    2. Player initializes input and output for interacting with player.
2. Puzzle displays current jumper status
    1. Gets input guess from player.
    2. Updates jumper with players guess.
    3. Checks jumper status.
        1. If word guessed, then display message to and quit.
        2. If no parachute left, then send game over message to player and quit.
        3. otherwise repeat loop at 'display current jumper status'


## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
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
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
* M. Scott Reynolds (mscottreynolds+github@gmail.com)
