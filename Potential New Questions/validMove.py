##Checking validity of a move[edit | edit source]
## Description of problem: When choosing where to move a piece, you must input the start square and finish square. If a valid start square is chosen, but an invalid destination square, the program will move on without prompting the player to re-enter.  

## Alter the code to prompt the user to re-enter the finish square until a valid square is given.

class Dastan:
    ...
    def PlayGame(self):
        ...
        MoveLegal = False  # change from SqureIsValid = False
        while not MoveLegal:  # change from while not SquareIsValid:
            FinishSquareReference = self.__GetSquareReference("to move to")
            SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)
            MoveLegal = self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, FinishSquareReference)  # bring MoveLegal check into while loop so that it asks until the Finish Square move is legal

        # remove if MoveLegal: as it is now guaranteed to be True
        PointsForPieceCapture = self.__CalculatePieceCapturePoints(FinishSquareReference)
        self._CurrentPlayer.ChangeScore(-(Choice + (2 * (Choice - 1))))
        self._CurrentPlayer.UpdateQueueAfterMove(Choice)
        self.__UpdateBoard(StartSquareReference, FinishSquareReference)
        self.__UpdatePlayerScore(PointsForPieceCapture)
        print("New score: " + str(self._CurrentPlayer.GetScore()) + "\n")

        ...
