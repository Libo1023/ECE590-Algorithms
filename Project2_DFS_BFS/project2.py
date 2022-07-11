"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1: Libo Zhang, NetID - lz200
Partner 2:
Date: November 2, 2021
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    ##### Your implementation goes here. #####
    # Implement Depth First Search.
    if alg == 'DFS' :
        # Initialize all values.
        for vertex in maze.adjList :
            # Set all visited values to False.
            vertex.visited = False
            # Set all prev values to None
            vertex.prev = None

        # Create an empty stack.
        stack = Stack()
        # Push the start vertex onto the stack.
        stack.push(maze.start)

        # While the stack is not empty...
        while not stack.isEmpty() :
            # Set current = stack.pop()
            current = stack.pop()
            if current.isEqual(maze.exit) :
                break

            if current.visited == False :
                current.visited = True
                # For each neighbor of current...
                for neighbor in current.neigh :
                    # Push it onto the stack.
                    stack.push(neighbor)
                    # If the neighbor has not yet been visited...
                    if neighbor.visited == False :
                        # Set its prev value to point at current.
                        neighbor.prev = current

        # Trace back the path from exit to start.
        pathback = [None for vertex in maze.adjList]
        current = maze.exit 
        rankback = 0
        while current != None :
            pathback[rankback] = current.rank 
            rankback = rankback + 1
            current = current.prev

        path_length = len(pathback)
        last_i = path_length - 1
        # Reverse the traceback path to find the correct path.
        correct_path = [pathback[i] for i in range(last_i, -1, -1) \
                                            if pathback[i] != None]
        # Assign the correct path to maze.path.
        maze.path = correct_path
        return maze.path

    # Implement Breadth First Search.
    if alg == 'BFS' :
        # Initialize all values.
        for vertex in maze.adjList :
            # Set all visited values to False.
            vertex.visited = False
            # Set all prev values to None.
            vertex.prev = None
            # Set all distance to infinity.
            vertex.dist = math.inf

        # Create an empty queue.
        queue = Queue()
        # Push the start vertex into the queue.
        queue.push(maze.start)
        # Set the start vertex distance as 0.
        maze.start.dist = 0

        # While the queue is not empty...
        while not queue.isEmpty() :
            # Set current = queue.pop().
            current = queue.pop()
            if current.isEqual(maze.exit) :
                break

            # For each neighbor of current...
            for neighbor in current.neigh :
                # If the neighbor has not yet been visited...
                if neighbor.dist == math.inf :
                    # Push it into the queue.
                    queue.push(neighbor)
                    neighbor.dist = current.dist + 1
                    # Set its prev value to point at current.
                    neighbor.prev = current
                    # Mark it as visited.
                    neighbor.visited = True

        # Trace back the path from exit to start.
        pathback = [None for vertex in maze.adjList]
        current = maze.exit
        rankback = 0
        while current != None :
            pathback[rankback] = current.rank 
            rankback = rankback + 1
            current = current.prev

        path_length = len(pathback)
        last_j = path_length - 1
        # Reverse the traceback path to find the correct path.
        correct_path = [pathback[j] for j in range(last_j, -1, -1) \
                                            if pathback[j] != None]
        # Assign the correct path to maze.path.
        maze.path = correct_path
        return maze.path 
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    #testMazes(False)
    testMazes(True)
