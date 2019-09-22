# Simulated-Annealing-Min-Conflicts_N_Queens
Implementation of the N-Queens problem by using Simulated Annealing as a local search algorithm and Min Conflicts as the CSP (Constraint Satisfaction Problem) algorithm.

### Prerequisites

Tested with python2.7 and Ubuntu 16.04.

### Run

To run the program open a terminal and : 
```
$ python2.7 app.py -N -algorith
```
Arguments :

+ N: the size of problem (NxN board), N-Queens

+ algorithm: choode -SA, or -MC for (Simulated annealing or Min conflicts)

### Output

The program returns :

+ Execution time
+ Number of Conflicts if there are any
+ Board with Queens as array in terminal
+ Create Images with queens on the board
