## New Move: TibbleCross
## Description of problem: The program is to be extended with a new type of move called the "TibbleCross". This move can allow a piece to go up two spaces diagonally from its starting position in any direction ( NW, NE, SE, SW ).

## Add this move so it appears first in the queue of moves for both players.

## Select the move and test it by selecting piece "22" and then moving to row/column "44"

def __CreateMoveOptionOffer(self):
    self._MoveOptionOffer.append("tibblecross") #append the new option
    self._MoveOptionOffer.append("jazair")
    self._MoveOptionOffer.append("chowkidar")
    self._MoveOptionOffer.append("cuirassier")
    self._MoveOptionOffer.append("ryott")
    self._MoveOptionOffer.append("faujdar")

def __CreateTibbleCrossMoveOption(self, Direction):
    NewMoveOption = MoveOption("tibblecross")
    NewMove = Move(2 * Direction,2 * Direction)
    NewMoveOption.AddToPossibleMoves(NewMove)
    NewMove = Move(-2 * Direction,2 * Direction)
    NewMoveOption.AddToPossibleMoves(NewMove)
    NewMove = Move(2 * Direction,-2 * Direction)
    NewMoveOption.AddToPossibleMoves(NewMove)
    NewMove = Move(-2 * Direction,-2 * Direction)
    NewMoveOption.AddToPossibleMoves(NewMove)
    return NewMoveOption

def __CreateMoveOption(self, Name, Direction):
    if Name == "tibblecross":
        return self.__CreateTibbleCrossMoveOption(Direction) ## add the move ##
    elif Name == "chowkidar":
        return self.__CreateChowkidarMoveOption(Direction)
    elif Name == "ryott":
        return self.__CreateRyottMoveOption(Direction)
    elif Name == "faujdar":
        return self.__CreateFaujdarMoveOption(Direction)
    elif Name == "jazair":
        return self.__CreateJazairMoveOption(Direction)
    else:
        return self.__CreateCuirassierMoveOption(Direction)

def __CreateMoveOptions(self):
    self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("tibblecross", 1)) ## add to player 1 ##
    self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("ryott", 1))
    self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("chowkidar", 1))
    self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("cuirassier", 1))
    self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("faujdar", 1))
    self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption("jazair", 1))

    self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("tibblecross", -1)) ## add to player 2 ##
    self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("ryott", -1))
    self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("chowkidar", -1))
    self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("jazair", -1))
    self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("faujdar", -1))
    self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption("cuirassier", -1))
