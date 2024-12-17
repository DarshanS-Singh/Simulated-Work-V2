# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:

# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.

# Problem link:- https://leetcode.com/problems/design-circular-deque/description/

# Solution Class

class MyCircularDeque:

    def __init__(self, k):
        self.q = []
        self.k = k
        
    def insertFront(self, value):
        if len(self.q) < self.k:
            self.q = [value] + self.q
            return True
        return False

    def insertLast(self, value):
        if len(self.q) < self.k:
            self.q.append(value) #push in last
            return True
        return False
        
    def deleteFront(self):
        if len(self.q) > 0:
            self.q.pop(0)
            return True
        return False

    def deleteLast(self):
        if len(self.q) > 0:
            self.q.pop()
            return True
        return False

    def getFront(self):
        if len(self.q) > 0:
            front = self.q[0]
            return front
        return -1

    def getRear(self):
        if len(self.q) > 0:
            last = self.q[-1]
            return last
        return -1
        
    def isEmpty(self):
        if len(self.q) == 0:
            return True
        return False
        
    def isFull(self):
        if len(self.q) == self.k:
            return True
        return False