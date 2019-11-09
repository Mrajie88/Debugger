import numpy as np
from generateCoverage import generateCoverage
from parseCoverage import ParseCoverage
from bubbleSort import BubbleSort
from NN import NN

def debug_statments(X,y):
    file_list,train_y = generateCoverage(BubbleSort,X,y,"BublleSort")
    print(train_y)
    train_X,lines = ParseCoverage("bubbleSort.py",file_list)
    print(train_X)
    statements_suspect = NN(train_X,train_y,(300),lines)
    print(lines)
    print(statements_suspect)
    print(lines[statements_suspect.tolist().index(np.max(statements_suspect))])
    print(np.max(statements_suspect))
    #return lines[]


if __name__ == '__main__':
    X = [[3,2,1,4,5,6],[4,4,4,4,4,4],[5,3,4,2,2,2],[10,2,3,1,1,1]]
    y = [[1,2,3,4,5,6],[4,4,4,4,4,4],[2,2,2,3,4,5],[1,1,1,2,3,10]]
    print(debug_statments(X,y))



