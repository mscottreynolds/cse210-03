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
Director
--------
_word: Current word and guess state.
_parachute: Current status of parachute.
_player: Player interface
start_game()

Word
----
_current_word
_current_state
create_word(): Create a new word.
make_guess(): Make a guess at a letter
display_word(): Display current state of word.
word_guessed(): Return true if word has been guessed.

Parachute
---------
_parachute_list
create_parachute(): Initialize parachute.
display_parachute(): Display current state of parachute.
cut_parachute(): Cut a line from parachute. Return true if not lost.
is_parachute(): Return true if still parachute left.

Player
------
new_player(): Initialize player. 
get_guess(): Player makes a guess at a letter.

```

### Sequence diagram.
1. Director initializes word, parachute, and player.
    1. Word reads random word from a list.
    2. Parachute creates full parachute state.
    3. Player initializes input and output for interacting with player. (Possibly a terminal class for io)
2. Loop. 
    1. Director displays current word and parachute status.
    2. Gets input guess from player.
    3. Updates word with guess.
    4. Checks word for guess. 
        1. If guessed, send won message to player.
        1. If not guessed, sends cut parachute message to parachute.
            1. if No parachute left, send game lost message to player.
    5. If word not guessed and still parachute left, repeat loop.
3. Game over.


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
