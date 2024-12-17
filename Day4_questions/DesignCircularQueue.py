# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Implement the MyCircularQueue class:

# MyCircularQueue(k) Initializes the object with the size of the queue to be k.
# int Front() Gets the front item from the queue. If the queue is empty, return -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language. 

# problem link:- https://leetcode.com/problems/design-circular-queue/description/

# Solution class

# Time Complexity: O(1)
# Space Complexity: O(N)
class MyCircularQueue:

    def __init__(self, k):
        # the queue holding the elements for the circular queue
        self.q = [0] * k
        # the number of elements in the circular queue
        self.cnt = 0
        # queue size
        self.sz = k
        # the idx of the head element
        self.headIdx = 0
        

    def enQueue(self, value):
        # handle full case
        if self.isFull(): return False
		# Given an array of size of 4, we can find the position to be inserted using the formula
		# targetIdx = (headIdx + cnt) % sz
		# e.g. [1, 2, 3, _]
		# headIdx = 0, cnt = 3, sz = 4, targetIdx = (0 + 3) % 4 = 3
		# e.g. [_, 2, 3, 4]
		# headIdx = 1, cnt = 3, sz = 4, targetIdx = (1 + 3) % 4 = 0
        self.q[(self.headIdx + self.cnt) % self.sz] = value
        # increase the number of elements by 1
        self.cnt += 1
        return True

    def deQueue(self):
        # handle empty case
        if self.isEmpty(): return False
        # update the head index
        self.headIdx = (self.headIdx + 1) % self.sz
        # decrease the number of elements by 1
        self.cnt -= 1
        return True

    def Front(self):
        # handle empty queue case
        if self.isEmpty(): return -1
        # return the head element
        return self.q[self.headIdx]
        
    def Rear(self):
        # handle empty queue case
        if self.isEmpty(): return -1
        # Given an array of size of 4, we can find the tail using the formula
        # tailIdx = (headIdx + cnt - 1) % sz
        # e.g. [0 1 2] 3
        # headIdx = 0, cnt = 3, sz = 4, tailIdx = (0 + 3 - 1) % 4 = 2
        # e.g. 0 [1 2 3]
        # headIdx = 1, cnt = 3, sz = 4, tailIdx = (1 + 3 - 1) % 4 = 3
        # e.g. 0] 1 [2 3
        # headIdx = 2, cnt = 3, sz = 4, tailIdx = (2 + 3 - 1) % 4 = 0
        return self.q[(self.headIdx + self.cnt - 1) % self.sz]

    def isEmpty(self):
        # no element in the queue
        return self.cnt == 0

    def isFull(self):
        # return True if the count is equal to the queue size
        # else return False
        return self.cnt == self.sz


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()