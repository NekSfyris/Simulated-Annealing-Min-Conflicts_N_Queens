from __future__ import print_function
from random import randint

class chessBoard(object):

    global qCols
    global Tconflicts
    global verbose


    #Constructor
    def __init__(self,N_Queens, verbose):
        global N
        global board

        board = []
        N = int(N_Queens)
        self.verbose = verbose


    # This creates the required board to sit our queens into.
    # The board is creating by using the supplied N during program initiation.
    def createBoard(self,state):
        i = 0
        self.qCols = state

        # Initialize the board
        for i in range(N):
        	temp=[]
        	for j in range(N):
        		temp.append(0)
        	board.append(temp)

        # Now put the queens in the board, please note that they are not in the same column.
        # This is ensured by the randomization above.
        for i in range(N):
            board[i][self.qCols[i]] = 1


    # This function updates the board Queen locations (should they change)
    def updateBoard(self):

        for i in range(N):
        	for j in range(N):
        		board[i][j]=0


        for i in range(N):
            board[i][self.qCols[i]] = 1


    # This function prints the supplied chess board based while aligning the columns and rows
    # This function was used only for the tests needed.
    # We have created a gui that picturize and saves in *.jpg format the resulting solution.
    def printBoard(self):
        #Print the rows of the chessBoard
        for x in board:
        	print(*x, sep=" ")


    #This function checks the chess board for any collisions that are present.
    def checkForConflicts(self):
        rRange = N-1
        self.Tconflicts = 0

        for i in range(rRange):
            for j in range(i+1, N):
                if(abs(i-j) == abs(self.qCols[i] - self.qCols[j])):
                    self.Tconflicts = self.Tconflicts + 1

    # This function creates a chess board, distributes the queens in it as well as prints it only if the user enables the
    # specific flag that does that
    def createAndEvalBoard(self, silent,state):

        self.createBoard(state)

        self.checkForConflicts()

    #This function is to convert the 2D matrix in a row matrix in order to visualize our solution
    #In the row matrix each cell contains a value. That value represents each queen's position row.
    #The queen's column position resulting from its index in the row matrix
    def prepareForVisualize(self):
    	grid=[]
    	for i in range(N):
    		for j in range(N):
    			if (board[i][j]==1):
    				grid.append(j)
    	return grid



# mboard=chessBoard(8,True)
# mboard.createBoard()
# mboard.printBoard()
# mboard.checkForConflicts()
# print(mboard.Tconflicts)
# grid=mboard.prepareForVisualize()
# print(mboard.qCols)
# print(grid)
# print(mboard.prepareForVisualize())
# for i in range(N):
# 	board
