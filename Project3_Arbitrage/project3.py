"""
Math 560
Project 3
Fall 2021

Partner 1: Libo Zhang (NetID: lz200)
Partner 2: Beibei Wu (NetID: mw515)
Date: Nov 3 2021
"""

# Import math and p3tests.
import math
from p3tests import *

# Indicate 80 characters in a line of code.
###############################################################################

"""
detectArbitrage: For detecting arbitrage in currency exchange

INPUT:
adjList: the adjacency list for storing vertices' neighbors
adjMat: the adjacency matrix for storing each edge's weight
tol: the precision

OUTPUT:
negCycle: a list of vertices in the detected negative cycle
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    # For all vertices:
    # Set the initial dist values to infinity.
    # Set the initial prev values to None.
    # The above initialization has been
    # completed in the Vertex constructor.

    # Set start.dist = 0.
    (adjList[0].neigh)[-1].dist = 0
    # Initialize the negative cost cycle list.
    negCycle = []

    # For each of the (|V| - 1) iterations:
    for i in range(len(adjList) - 1):
        # For each vertex in the graph:
        for j in range(len(adjList)):
            neighs = adjList[j].neigh
            # For each neighbor of each vertex:
            for neigh in neighs:
                # Update each neighbor of current vertex using
                # current vertex's dist and the edge weight
                # between them when accepting.
                # Only update if the new value is better! 
                if neigh.dist > adjList[j].dist + adjMat[j][neigh.rank] + tol:
                    # Accept.
                    # Update distance.
                    neigh.dist = adjList[j].dist + adjMat[j][neigh.rank]
                    # Update previous vertex.
                    neigh.prev = adjList[j]
    
    # 1 more iteration to detect negative cost cycle (arbitrage).
    flag = 0
    temp = None
    # For each vertex in the graph:
    for u in adjList:
        neighs = adjList[u.rank].neigh
        # For each neighbor of each vertex:
        for neigh in neighs:
            # If there is still one "better value" to update
            # at iteration (|V|), then we find one arbitrage.
            if neigh.dist > u.dist + adjMat[u.rank][neigh.rank] + tol:
                # Accept
                # Mark that there is one negative cost cycle.
                flag = 1
                neigh.dist = u.dist + adjMat[u.rank][neigh.rank]
                neigh.prev = u
                temp = neigh
    if flag == 1:
        some = temp.prev

        # About list insert, append, and reverse methods:
        # Two ways to find the correct arbitrage opportunity.
        # First, since we are always tracking the previous vertex,
        # after appending prev vertex to the negCycle list,
        # we need to reverse this backward path.

        # Second, we could always insert the prev vertex at the 
        # beginning of the negCycle list, therefore saving effort 
        # for final reversing.
        negCycle.insert(0, temp.rank)
        #negCycle.append(temp.rank)

        while not some.isEqual(temp):

            negCycle.insert(0, some.rank)
            #negCycle.append(some.rank)

            some = some.prev

        negCycle.insert(0, some.rank)
        #negCycle.append(some.rank)
        
    #negCycle.reverse()
    return negCycle
    ##### Your implementation goes here. #####

###############################################################################
# Indicate 80 characters in a line of code.

"""
rates2mat: calculating the needed adjacency matrix

INPUT:
rates: a 2D matrix storing the exchange rates between any two currencies

OUTPUT:
return an adjacency matrix adjusted for a bellman ford problem
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # (-1) * log(R(u, v))
    # We use logarithmic values as edge weights.
    return [[(-1)*math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
