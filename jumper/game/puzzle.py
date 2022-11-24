import random
from game.terminal_service import TerminalService


class Puzzle:
    """
    Puzzle
    ----
    make_guess(): Make a guess at a letter. Return true if the letter is correct.
    display_puzzle(): Display the current state of the word.
    is_puzzle_solved(): Return true if the word has been guessed.
    """

    def __init__(self):
        random_word_list = ['Hinge','Sepia','Short','Stove','Peter','Codex']
        random_word = random.choice(random_word_list)

        self._puzzle_word = random_word
        self._guesses = ['_'] * len(self._puzzle_word)

    def display_puzzle(self, terminal):
        terminal.write_text(' '.join(self._guesses))
        terminal.write_text('')

    def make_guess(self, letter):
        # Check the letter to see if it is in the word.
        # Update list of correct guesses.
        # Returns: True if guess is correct.
        puzzle_word = self._puzzle_word
        guesses = self._guesses
        guess_correct = False
        guess = letter.upper()
        for index in range(len(puzzle_word)):
            if guesses[index] == '_' and guess == puzzle_word[index].upper():
                guess_correct = True
                guesses[index] = puzzle_word[index]

        return guess_correct


    def is_puzzle_solved(self):
        # Check to see if the puzzle has been solved. 
        # Returns True if there aren't any '_' characters in the _guesses list.
        return not '_' in self._guesses
