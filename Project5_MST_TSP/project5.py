"""
Math 560
Project 5
Fall 2021

Partner 1: Beibei Wu (NetID: mw515)
Partner 2: Libo Zhang (NetID: lz200)
Date: November 28, 2021
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

# 80 characters in a line of code.
###############################################################################

"""
Prim's Algorithm

This function will take as input the adjList and adjMat of 
the Map class, and it has no outputs. 
This function will ensure that at the end of execution, 
every vertex has been assigned the proper vertex.prev values.

"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####

    # The initialization of all costs to infinity
    # and prev to null has been implemented in the
    # Vertex constructor, so we do not need to
    # initialize again here in prim function.

    # Pick an arbitrary start vertex and set cost to 0.
    # Here we pick the first vertex as the start vertex.
    adjList[0].cost = 0

    # Make the priority queue using cost for sorting.
    Q = PriorityQueue(adjList)

    # While the priority queue is not empty:
    while not Q.isEmpty():
        # Get the next unvisited vertex and visit it.
        minVal = Q.deleteMin()
        minVal.visited = True

        # For each edge out of minVal vertex:
        for neigh in minVal.neigh:

            # If the edge leads out, update.
            if not neigh.visited:
                if neigh.cost > adjMat[minVal.rank][neigh.rank]:
                    neigh.cost = adjMat[minVal.rank][neigh.rank]
                    neigh.prev = minVal
                    
# 80 characters in a line of code.
###############################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.

This function will take as input the adjList and 
(already sorted) edgeList of the Map class, and 
it will return a list of edges that are in the MST.

"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####

    # Initialize all singleton sets for each vertex.
    for item in adjList:
        makeset(item)

    # Initialize the empty MST.
    X = []

    # Sort the edges by weight.
    # Since the edgeList has already been sorted, 
    # we do not need to sort again here in Kruskal function.
    # edgeList.sort()

    # Loop through the edge in increasing order.
    for e in edgeList:

        # If the min edge crosses a cut, add it to our MST.
        u, v = e.vertices
        if find(u) != find(v):
            X.append(e)

            # Union two Disjoint Sets into one Disjoint Set.
            union(u, v)

    return X

# 80 characters in a line of code.
###############################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    ##### Your implementation goes here. #####
    # Make each vertex itself as one Disjoint Set.

    # Each tree corresponds to a set of connected vertices.
    # The root of the tree is the value used to identify the set.

    # The parent pointer of v points to v itself, 
    # and the tree height is initially 0.
    v.pi = v
    v.height = 0
    return 

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    ##### Your implementation goes here. #####
    if v != v.pi:
        # Use recursive calls to achieve Path Compression.
        # The recursive calls terminate when finding
        # the root of the tree.
        v.pi = find(v.pi)
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ##### Your implementation goes here. #####

    # Find the root of the Disjoint Set of u.
    ru = find(u)
    # Find the root of the Disjoint Set of v.
    rv = find(v)

    # If their Disjoint Sets are the same, 
    # then there is no need for union operation.
    if ru == rv:
        return

    # We should keep the tree as short as possible.
    # The root vertex of a shorter Disjoint Set tree
    # should points to the root vertex of a taller
    # Disjoint Set tree so that we do not need to
    # increase the tree height after union operation.
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    # If the two Disjoint Sets have the same tree height, 
    # then we break the tie and increase the tree height
    # by 1 for the new Disjoint Set after union operation.
    else:
        ru.pi = rv
        rv.height += 1
    return

# 80 characters in a line of code.
###############################################################################

"""
TSP

This function will be given the Map's adjList 
and start attributes as inputs, and must return
the tour array of vertex ranks.

"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####

    # Initialize an empty tour list.
    tour = []

    # Implement Depth First Search (DFS).

    # Initialize all values.
    for item in adjList:
        # Set all visited values to False.
        item.visited = False
        # We do not need the prev values,
        # so we leave prev values unchanged.

    # Create an empty stack.
    # In Python, lists work exactly like stacks.
    s = [] # stack

    # Mark the start vertex as visited and 
    # push it onto the stack.
    start.visited = True
    s.append(start)

    # While the stack is not empty:
    while s:
        # Set current = stack.pop().
        current = s.pop()
        # For each MST neighbor of current vertex:
        for mstNeigh in current.mstN:
            # If the MST neighbor has not yet been visited:
            if not mstNeigh.visited:
                # Mark it as visited.
                mstNeigh.visited = True
                # Push it onto the stack.
                s.append(mstNeigh)
        # Follow the Depth First Search path, 
        # append the current vertex rank into the tour list.
        tour.append(current.rank)
    # Finally, append the start vertex rank again
    # to complete the tour cycle.
    tour.append(start.rank)
    return tour

# 80 characters in a line of code.
###############################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
