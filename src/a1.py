from __future__ import division
import copy


#create initial state of board
def take_input():
    #Accepts the size of the chess board


    #take board size
    while True:
        try:
            size = int(input('What is the size of the chessboard? n = '))
            if size == 1:
                print("Trivial solution, choose a board size of atleast 4")
            if size <= 3:
                print("Enter a value such that size>=4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")

def get_board(size):

    #Returns an n*n board
    board = [0]*size
    for ix in range(size):
        board[ix] = [0]*size
    return board

############################################

#put each queens size
def queens_input(size):
    #Accepts the queens positions

    x=0;

    #initialissing state
    queens = [0]*size

    #until all queens are properly placed
    while x<size:

        #in case of exception
        try:
            queens[x] = int(input('What is the number {} queens position on the chessboard? n = '.format(x)))
            if queens[x]/10 < 1:
                print("Enter a value like 12, which means the queen is on the 1rst row, on the 2nd column")
            x=x+1;
        except ValueError:
            print("Invalid value entered. Enter again")

    #returning with queens states
    return queens


############################################

#find conflicts and print which of the following conflicts are happening
def is_not_safe(board, row, col, size):
    #Check if it's safe to place a queen at board[x][y]

    #------------checking rows------------
    #check left row of queen
    for iy in range(col):
        if board[row][iy] == 1:
			print '1'
			return False

    
    #check right row of queen
    for iy in range(col+1,size):
        if board[row][iy] == 1:
			print "2"
			return False

    #------------checking columns------------
    #check up of queen column
    for iy in range(row):
        if board[iy][col] == 1:
            print '3'
            return False

    
    #check down of queen column
    for iy in range(row+1,size):
        if board[iy][col] == 1:
            print "4"
            return False
    

	#-----------checking diagonial \----------
    #check point to back diagonial
    ix, iy = row-1, col-1
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
			print "5"
			return False
        ix-=1
        iy-=1
    
    #check point to end diagonial
    ix, iy = row+1, col+1
    while ix <= size and iy <= size:
        if board[ix][iy] == 1:
			print "6"
			return False
        ix+=1
        iy+=1

    #-----------checking diagonial /----------
	#check point to down diagonial
    jx, jy = row+1,col-1
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
			print "7"
			return False
        jx+=1
        jy-=1
    
    #check point to end diagonial
    jx, jy = row-1,col+1
    while jx >= 0 and jy < size:
        if board[jx][jy] == 1:
			print "8"
			return False
        jx-=1
        jy+=1

    return True

#find total conflicts
def solve(board, size):
   
   #put queens on board position
    x=0;
    y=0;
    count=0;
    for i in range(size):
    	x=(queens[i]//10)-1
    	y=(queens[i]%10)-1
    	board[x][y]=1
    
    #print the board as a 0 for no queen in position, and 1 for existing queen in position
    solutions = []
    #first copy and then print board
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)
    for sol in solutions:
        for row in sol:
            print(row)
        

    #find if conflicts exist for each queen
    for i in range(size):
    	
    	x=(queens[i]//10)-1
    	#print x
    	y=(queens[i]%10)-1
    	#print y

        #if a conflict occurs then add one to total counter
    	if is_not_safe(board, x, y, size-1)==False:
    		count=count+1;

    print('\nTotal conflicts : {}'.format(count))

#start by taking board size
size = take_input()

#create board of given size
board = get_board(size)

#place each of the queens on board
queens = queens_input(size)

#find conflicts
solve(board, size)