from game.terminal_service import TerminalService


class Jumper:
    """
    Jumper
    ---------
    display_jumper(): Display the current state of the jumper and parachute.
    cut_parachute(): Cut a line from the parachute.
    is_parachute(): Return true if there is some parachute left.
    """


    def __init__(self):
        # Initialize the jumper and set values for parachute start and end.

        # These constants define the jumper and the parachute starting and ending line positions.
        self._jumper = [
            '  ___  ',
            ' /___\ ',
            ' \   / ',
            '  \ /  ',
            '   O   ',
            '  /|\  ',
            '  / \  ',
            '       ',
            '^^^^^^^']
        self._parachute_start = 0
        self._parachute_end = 3
        self._game_over = \
            '   x   '
        self._game_over_position = 4

        # This keeps track of the players current "cut" position. When it is greater than
        # the parachute END position, the game is over.
        self._cut_position = 0
        

    def display_jumper(self, terminal):
        # Display jumper, starting at the players cut position.
        for line in range(self._cut_position, len(self._jumper)):
            terminal.write_text(self._jumper[line])
        terminal.write_text('')


    def cut_parachute(self):
        # 'Cut' a line from the parachute.
        if self._cut_position <= self._parachute_end:
            self._cut_position += 1
        
        if not self.is_parachute():
            # Game over. Replace the jumper's head with game over indicator.
            self._jumper[self._game_over_position] = self._game_over


    def is_parachute(self):
        # Return true if there is still some parachute left.
        return self._cut_position <= self._parachute_end
