"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1: Libo Zhang, NetID - lz200
Partner 2:
Date: November 2, 2021
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        stack_length = len(self.stack)
        if self.numElems == stack_length :
            # Return true when the stack is full.
            return True
        else :
            # Otherwise, return false.
            return False

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0 :
            # Return true when the stack is empty.
            return True
        else :
            # Otherwise, return false.
            return False

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        # Use Python list comprehension to resize the stack
        # by doubling the size of the array.
        self.stack = self.stack + [None for element in self.stack]
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        # When the stack is full, resizing is required.
        if self.isFull() :
            self.resize()
        
        # Take in some value and push it onto the top of the stack.
        self.top = self.top + 1
        self.stack[self.top] = val
        self.numElems = self.numElems + 1
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        # Pop the top value off the stack.
        top_value = self.stack[self.top]
        self.stack[self.top] = None
        self.top = self.top - 1
        self.numElems = self.numElems - 1
        # Return the top value.
        return top_value
