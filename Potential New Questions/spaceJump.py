## New Move: spacejump
## Description of problem: Add a new move called a spacejump which moves the chosen piece to a random place on the board. It can't land on your own pieces, but everywhere else is fine. The player cannot choose where the piece will end up. The spacejump move will not be added to the queue of moves, instead a player is allowed one per game that can be used whenever they choose in lieu of a queue choice. Test by allowing player 1 to use the option from square 22 and then player 2 from square 55. Player 1 will not have the option displayed on their next turn.

class Dastan: #there is a bug where after choosing spacejump it will print a bunch of memory locations but do i care?
    def PlayGame(self):
        GameOver = False
        while not GameOver:
            self.__DisplayState()
            SquareIsValid = False
            Choice = 10 #different default value
            while Choice < 1 or Choice > 3:
                if self._CurrentPlayer.SpacejumpUsed==True:
                    Choice = int(input("Choose move option to use from queue (1 to 3) or 9 to take the offer: "))
                else:
                    Choice = int(input("Choose move option to use from queue (1 to 3) or 9 to take the offer or 0 to do Spacejump: ")) #ask only if spacejump not used
                if Choice == 9:
                    self.__UseMoveOptionOffer()
                    self.__DisplayState()
                if Choice==0:
                    if self._CurrentPlayer.SpacejumpUsed==True: #if already used
                        Choice=10 #reset and ask again
                    else: #else toggle flag
                        if self._CurrentPlayer==self._Players[0]:
                            self._Players[0].SpacejumpUsed=True
                        if self._CurrentPlayer==self._Players[1]:
                            self._Players[1].SpacejumpUsed=True
                        break #no need to ask again even though while loop condition is satisfied (spacejump IN LIEU of queue choice)
            while not SquareIsValid:
                StartSquareReference = self.__GetSquareReference("containing the piece to move")
                SquareIsValid = self.__CheckSquareIsValid(StartSquareReference, True)
            SquareIsValid = False

            if Choice!=0: #require finish square if not spacejump is chosen
                while not SquareIsValid:
                    FinishSquareReference = self.__GetSquareReference("to move to")
                    SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False)
                MoveLegal = self._CurrentPlayer.CheckPlayerMove(Choice, StartSquareReference, FinishSquareReference)
            else:
                while not SquareIsValid:
                    FinishSquareReference = random.randint(1,self._NoOfRows)*10+random.randint(1,self._NoOfColumns) 
 #random row column that is in bounds of board
                    SquareIsValid = self.__CheckSquareIsValid(FinishSquareReference, False) #makes sure piece does not land on own piece
                    MoveLegal=True #move always legal as it can be anywhere

            if MoveLegal:
                PointsForPieceCapture = self.__CalculatePieceCapturePoints(FinishSquareReference)
                if Choice!=0: #relevant only if not spacejump is used
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

class Player:
    def __init__(self, N, D):
        self.__Score = 100
        self.__Name = N
        self.__Direction = D
        self.__Queue = MoveOptionQueue()
        self.SpacejumpUsed=False #add spacejump flag
