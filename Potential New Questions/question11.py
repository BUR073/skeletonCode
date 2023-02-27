## Question 11
## Description of problem: Currently you can crash the game when asked to choose "use from queue (1 to 3) or 9 to take the offer" by entering non-integer input.

## Validate user input forcing it to be an integer, for choosing 1, 2, 3 or 9, and, if 9 was chosen, for then choosing the move option to replace. A good way to do this is to write a method __ValidateUserInput(PromptString) in the Dastan class, and call this method in PlayGame, passing it the required prompt strings in the two situations where it needs to be called. The method should return the user's input. For now, I would not validate whether it is an appropriate integer, just that it is in fact an integer. To do this you will need to use try ... except ValueError, and a while loop.

 def __GetSquareReference(self, Description):
        ###  ADDED  ###
        SelectedSquare = 0
        try:
            SelectedSquare = int(input("Enter the square " + Description + " (row number followed by column number): "))
        except ValueError:
            pass
        ###  END   ###
        return SelectedSquare

    
def __UseMoveOptionOffer(self):
        ### ADDED   ###
        val = True
        while val:
            try:
               ReplaceChoice = int(input("Choose the move option from your queue to replace (1 to 5): "))
            except ValueError:
                continue
            if 0 < ReplaceChoice < 6:
                val = False
            else:
                continue
        ###   END   ###

    
def PlayGame(self):
        GameOver = False
        while not GameOver:
            self.__DisplayState()
            SquareIsValid = False
            Choice = 0
            while Choice < 1 or Choice > 3:
                ###   ADDED   ###
                try:
                    Choice = int(input("Choose move option to use from queue (1 to 3) or 9 to take the offer: "))
                except ValueError:
                    continue
                ###   END   ###

    
def PlayGame(self):
        GameOver = False
        while not GameOver:
        [...]
            while not SquareIsValid:
                FinishSquareReference = self.__GetSquareReference("to move to")
                SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)
                ###   ADDED   ###
                MoveLegal = self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, FinishSquareReference)
                if MoveLegal == False:
                    SquareIsValid = False
                else:
                    SquareIsValid = True
                ###   END   ###
