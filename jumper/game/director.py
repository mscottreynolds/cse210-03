from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle
from game.player import Player


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    """

    def __init__(self):
        """
        Initialize jumper, puzzle, and player.
        """
        self._terminal = TerminalService()
        self._puzzle = Puzzle()
        self._jumper = Jumper()
        self._player = Player()
        self._is_playing = True
        

    def start_game(self):
        """Starts the game by running the main game loop."""
        self._display_state()
        while self._is_playing:
            self._do_updates()
            self._check_state()
            self._display_state()


    def _display_state(self):
        """Display the state of the puzzle and the jumper."""

        terminal = self._terminal
        terminal.write_text('')
        self._puzzle.display_puzzle(terminal)
        self._jumper.display_jumper(terminal)


    def _do_updates(self):
        """Get a letter guess from the player and update puzzle and jumper."""

        letter = self._player.guess_a_letter(self._terminal)
        if not self._puzzle.make_guess(letter):
            self._jumper.cut_parachute()


    def _check_state(self):
        """Check the state of the puzzle and parachute. Display results to player. Update is_playing flag."""

        terminal = self._terminal
        if self._puzzle.is_puzzle_solved():
            terminal.write_text("You won!")
            self._is_playing = False
        elif not self._jumper.is_parachute():
            terminal.write_text("Sorry game lost.")
            self._is_playing = False


