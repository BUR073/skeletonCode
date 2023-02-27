## New Move: rook[edit | edit source]
## Description of problem: Add a new move which moves forward until the piece hits the end of the board or hits another piece

while not SquareIsValid:
            StartSquareReference = self.__GetSquareReference("containing the piece to move")
            SquareIsValid = self.__CheckSquareIsValid(StartSquareReference, True)
            SquareIsValid = False
          
            #this is what changed   
            while not SquareIsValid:
               
                if self._CurrentPlayer.GetQueue(Choice) == "castle":
                    SquareIsValid = True
                    
                    FinishSquareReference = StartSquareReference
                    while SquareIsValid:
                        
                        FinishSquareReference =int(str((int(str(FinishSquareReference)[0])+(1)*self._CurrentPlayer.GetDirection()))+str(FinishSquareReference)[1])
                        
                        
                        SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)
                        if SquareIsValid == False:
                            FinishSquareReference =int(str((int(str(FinishSquareReference)[0])-(1)*self._CurrentPlayer.GetDirection()))+str(FinishSquareReference)[1])
                            
                        elif ( self.__CalculatePieceCapturePoints(FinishSquareReference))!=0:
                           
                            FinishSquareReference =int(str((int(str(FinishSquareReference)[0])-(1)*self._CurrentPlayer.GetDirection()))+str(FinishSquareReference)[1])
                            SquareIsValid = True
                            break
                else:
                    FinishSquareReference = self.__GetSquareReference("to move to")
                if SquareIsValid == False:
                    SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)
            #this is the end of what is changed    
                
    
                    
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
def GetQueue(self,Pos):
        Temp = self.__Queue.GetMoveOptionInPosition(Pos - 1).GetName()
        return Temp
