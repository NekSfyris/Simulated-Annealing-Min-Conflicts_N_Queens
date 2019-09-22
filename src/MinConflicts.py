import time
import sys
import random

Iterations=1000




#return a random number in N based on expression
#find a random column with hits more than 0
def rndm_col(li,N):
    return random.choice([i for i in range(N) if (li[i]>0)])


#return a random number in N based on expression
#random min of row for current column
def rndm_min(li,N):
    return random.choice([i for i in range(N) if (li[i]==min(li)) ])



def min_conflicts(listN, N, iters=Iterations):

    #for p in listN: print (p)

    #number of iterations it will search to find no hitting queens
    for k in range(iters):

        #we store the starting hits as a list
        starting_conflicts = find_conflicts(listN, N)
        #print (starting_conflicts)

        #if we somehow managed to solve all hits then we return to show our solution
        #otherwise we send ou final instance of the problem
        if sum(starting_conflicts) == 0 or k==iters-1:
            return k,listN,sum(starting_conflicts)

        #take the random column with hits more than 0
        column = rndm_col(starting_conflicts,N)

        #for a known column, try to find hits in all the rows for this column
        each_conflicts = [hits(listN, N, column, row) for row in range(N)]

        #update the main lists element in the column we've been searching for,
        #with its new position in row and column.
        #the queens column is column and row listN[column]
        listN[column] = rndm_min(each_conflicts,N)

    #in case we didnt solve it with current iterations maybe we just needed more
    # raise ValueError("Maybe you needed more iterations. Number of hits remaining is " ,sum(confs))

#first try to find hits
def find_conflicts(listN, N):

    #We start with a pseudo-random placement of queens at (i,i).
    #Call following function N times. Each time we change column.
    #We initialize the cell hits too for that placement.
    return [hits(listN, N, column, listN[column]) for column in range(N)]

#here we want to find the number of hits for each cell in board
def hits(listN, N, column, row):

    # initialize counter
    hit_counter = 0
    #search for each column
    for i in range(N):
        #then we talk about the column our queen is which
        #we are searching for. So we continue
        if i == column:
            continue

        #known the starting positions of all queens, we search if the
        #position we currently are, is being "hit" by other queens.
        #Which means either they are on the same row or diagonial, but they
        #are certainly not in the same column
        if listN[i] == row or abs(i - column) == abs(listN[i] - row):
            hit_counter += 1
            #print(column,i,hit_counter)

    return hit_counter

def successorFunction(IState, Psize):
    start_time=time.time()
    iters,sol,Tcols=min_conflicts(IState,Psize)
    end_time=time.time()
    print('\nMC Stats:\n\tIterations: ' + str(iters) + " out of: " + str(Iterations))
    print('\n\tTotal Collisions (so far): ' + str(Tcols) + '\n\t' + str(('We did not find a solution','We found a solution')[Tcols == 0]))

    return sol,(end_time - start_time),Tcols,Iterations
