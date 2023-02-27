## UserName input
## At the beginning of the game allow each user to enter their own name to be used as a replacement to "Player One" and "Player Two"

class Dastan:
    def __init__(self, R, C, NoOfPieces):
        self._Board = []
        self._Players = []
        self._MoveOptionOffer = []
        playerOneName = input("Please enter player 1's name: ")
        self._Players.append(Player(playerOneName, 1))
        playerTwoName = input("Please enter player 2's name: ")
        self._Players.append(Player(playerTwoName, -1))
        self.__CreateMoveOptions()
