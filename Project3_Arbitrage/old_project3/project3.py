"""
Math 560
Project 3
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
    ## initial:
    (adjList[0].neigh)[-1].dist = 0
    negCycle = []
    ## |V| - 1 iterations
    for i in range(len(adjList) - 1):
        for j in range(len(adjList)):
            neighs = adjList[j].neigh
            for neigh in neighs:
                if neigh.dist > adjList[j].dist + adjMat[j][neigh.rank] + tol:
                    ## accept

                    # Modify Part 1

                    # neigh.dist = adjList[j] + adjMat[j][neigh.rank]
                    neigh.dist = adjList[j].dist + adjMat[j][neigh.rank]
                    neigh.prev = adjList[j]
    
    ## 1 iteration to detect negative cycle
    flag = 0
    temp = None
    for u in adjList:
        neighs = adjList[u.rank].neigh
        for neigh in neighs:
            if neigh.dist > u.dist + adjMat[u.rank][neigh.rank] + tol:
                ## accept
                flag = 1
                neigh.dist = u.dist + adjMat[u.rank][neigh.rank]
                neigh.prev = u
                temp = neigh
    if flag == 1:
        some = temp.prev
        negCycle.append(temp.rank)
        # print(temp.rank)
        # print("###")
        while not some.isEqual(temp):
            # print("******")
            # print(some.rank)
            negCycle.append(some.rank)
            some = some.prev
        negCycle.append(some.rank)
        # print(negCycle)

    # Modify Part 2

    negCycle.reverse()
    # print(negCycle)
    # print(negCycle.reverse())

    return negCycle
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    return [[(-1)*math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
