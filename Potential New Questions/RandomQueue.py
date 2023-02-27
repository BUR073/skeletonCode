## Random start queue
## Description of problem: Randomize the players move queue at the beginning of the game so that the players do not start with the same queue at the beginning of every game.

def __CreateMoveOptions(self):
    #creates a list of all possible moves
    list = ["ryott","chowkidar","cuirassier","lazzad","jazair"]
    #random.shufflle will randomize the list contents
    random.shuffle(list)
    #the  for loop will iterate through each of the contents of thh list
    for i in list:
        #and will add the moves to the move options
        self._Players[0].AddToMoveOptionQueue(self.__CreateMoveOption(i, 1))
        self._Players[1].AddToMoveOptionQueue(self.__CreateMoveOption(i, -1))
            
