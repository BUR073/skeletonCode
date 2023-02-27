## Show where the piece can move
## Description of problem: At the moment when selecting a move the player is expected to remember the ways in which move can be applied. Modify the program so that, once a piece has been selected a '^' symbol appears in the squares into which that piece can be moved based on the move selected. - Resolve using method A1 specification

    def __DisplayMove(self, CurrentPlayer, Choice, StartSquareReference):
        print("\n" + "   ", end="")
        for Column in range(1, self._NoOfColumns + 1):
            print(str(Column) + "  ", end="")
        print("\n" + "  ", end="")
        for Count in range(1, self._NoOfColumns + 1):
            print("---", end="")
        print("-")
        for Row in range(1, self._NoOfRows + 1):
            print(str(Row) + " ", end="")
            for Column in range(1, self._NoOfColumns + 1):
                Index = self.__GetIndexOfSquare(Row * 10 + Column)
                print("|" + self._Board[Index].GetSymbol(), end="")
                PieceInSquare = self._Board[Index].GetPieceInSquare()
                if self.__CheckSquareIsValid(Row * 10 + Column, False) and CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, Row * 10 + Column):
                    print("^", end="")
                elif PieceInSquare is None:
                    print(" ", end="")
                else:
                    print(PieceInSquare.GetSymbol(), end="")
            print("|")
        print("  -", end="")
        for Column in range(1, self._NoOfColumns + 1):
            print("---", end="")
        print()
        print()


    def PlayGame(self):
            ...
            SquareIsValid = False
            self.__DisplayMove(self._CurrentPlayer,Choice,StartSquareReference)
            ...
    
    #~Victor
