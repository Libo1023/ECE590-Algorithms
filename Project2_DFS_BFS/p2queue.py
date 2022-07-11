"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1: Libo Zhang, NetID - lz200
Partner 2:
Date: November 2, 2021
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        queue_length = len(self.queue)
        if self.numElems == queue_length :
            # Return true when the queue is full.
            return True
        else :
            # Otherwise, return false.
            return False

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0 :
            # Return true when the queue is empty.
            return True
        else :
            # Otherwise, return false.
            return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        # Unwrapping the queue.
        if self.front >= self.rear :
            self.queue = self.queue[self.front:] + self.queue[:self.rear]
        # Reset front and rear values.
        self.front = 0
        self.rear = self.numElems
        # Use Python list comprehension to resize the queue
        # by doubling the size of the array.
        self.queue = self.queue + [None for element in self.queue]
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        # When the queue is full, resizing is required.
        if self.isFull() :
            self.resize()

        # Take in some value and push it into the rear of the queue.
        self.queue[self.rear] = val

        # Update rear and numElems.
        queue_length = len(self.queue)
        if self.rear == (queue_length - 1) :
            self.rear = 0
        else :
            self.rear = self.rear + 1

        self.numElems = self.numElems + 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        # Pop the front value from the queue.
        front_value = self.queue[self.front]
        self.queue[self.front] = None

        # Update front and numElems.
        queue_length = len(self.queue)
        if self.front == (queue_length - 1) :
            self.front = 0
        else :
            self.front = self.front + 1

        self.numElems = self.numElems - 1
        # Return the front value.
        return front_value

