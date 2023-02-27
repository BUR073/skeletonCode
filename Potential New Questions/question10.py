## Question 10
## Description of problem: Currently, if a player accepts the move option offer (so for example, player 1 takes the jazair offer and replaces the ryott), they then get exactly the same choices again: Choose move option to use from queue (1 to 3) or 9 to take the offer:. This is what the Preliminary Material says will happen "Taking the move option from the offer does not count as a move" ... it is still that player's turn. However, your challenge is to change this, so it DOES count as a turn, and if they choose 9, it goes on to the next player.

def PlayGame(self):
        GameOver = False
        while not GameOver:
            self.__DisplayState()
            SquareIsValid = False
            Choice = 0
            while Choice < 1 or Choice > 3:
                Choice = int(input("Choose move option to use from queue (1 to 3) or 9 to take the offer: "))
                if Choice == 9:
                    #---------
                    #put it before to change player before board is displayed again
                    if self._CurrentPlayer.SameAs(self._Players[0]):
                        self._CurrentPlayer = self._Players[1]
                    else:
                        self._CurrentPlayer = self._Players[0]
                    #---------
                    self.__UseMoveOptionOffer()
                    self.__DisplayState()
            while not SquareIsValid:
                StartSquareReference = self.__GetSquareReference("containing the piece to move")
                SquareIsValid = self.__CheckSquareIsValid(StartSquareReference, True)
            SquareIsValid = False
            while not SquareIsValid:
                FinishSquareReference = self.__GetSquareReference("to move to")
                SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)
            MoveLegal = self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, FinishSquareReference)
            if MoveLegal:
                PointsForPieceCapture = self.__CalculatePieceCapturePoints(FinishSquareReference)
                self._CurrentPlayer.ChangeScore(-(Choice + (2 * (Choice - 1))))
                self._CurrentPlayer.UpdateQueueAfterMove(Choice)
                self.__UpdateBoard(StartSquareReference, FinishSquareReference)
                self.__UpdatePlayerScore(PointsForPieceCapture)
                print("New score: " + str(self._CurrentPlayer.GetScore()) + "\n")
            if self._CurrentPlayer.SameAs(self._Players[0]):
                self._CurrentPlayer = self._Players[1]
            else:
                self._CurrentPlayer = self._Players[0]
            GameOver = self.__CheckIfGameOver()
        self.__DisplayState()
        self.__DisplayFinalResult()
