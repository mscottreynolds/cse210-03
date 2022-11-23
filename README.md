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
The game is controlled by a Director class. The director maintains the Word and Parachute classes, however leaving the implementation of each to the individual classes. Director also creates a class for the Player which will be used to get input from the player. This allows the Player class to encapsulate how it actually gets input from the user.

As a convenience, Director may create a utility class that represents terminal IO that will be used when communicating with the player and displaying the status of the word and parachute.

### Class diagram
```
Director
--------
_word: Current word and guess state.
_parachute: Current status of the parachute.
_player: Player interface
start_game()

Word
----
_current_word
_current_state
create_word(): Create a new word.
make_guess(): Make a guess at a letter. Return true if the letter is correct.
display_word(): Display the current state of the word.
word_guessed(): Return true if the word has been guessed.

Parachute
---------
_parachute_list
create_parachute(): Initialize parachute.
display_parachute(): Display the current state of the parachute.
cut_parachute(): Cut a line from the parachute. Return true if not lost.
is_parachute(): Return true if still parachute left.

Player
------
new_player(): Initialize player.
get_guess(): Player makes a guess at a letter.

```

### Sequence diagram.
1. Director initializes word, parachute, and player.
    1. Word reads a random word from a list.
    2. Parachute creates a full parachute state.
    3. Player initializes input and output for interacting with the player. (Possibly a terminal class for io)
2. Loop.
    1. Director displays the current word and parachute status.
    2. Gets input guess from the player.
    3. Updates word with the guess.
    4. Checks the word for a correct guess.
        1. If guessed, send a won message to the player.
        1. If not guessed, send a cut parachute message to the parachute.
            1. If no parachute is left, send a game lost message to the player.
    5. If the word is not guessed and still parachute left, repeat the loop.
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
    +-- word.py         (contains word puzzle)
    +-- parachute.py    (represents the parachute of the jumper.)
    +-- player.py       (represents the player.)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8

## Authors
* M. Scott Reynolds (mscottreynolds+github@gmail.com)
