from game.terminal_service import TerminalService

class Player:
    """The class that represents the player. Handles getting input from the player.
    """

    def __init__(self):
        # nothing to do for now.
        return
       
    def guess_a_letter(self, terminal):
        """Player guesses and returns a letter.
        """
        letter = terminal.read_text("Guess a letter [a-z]")
        return letter
