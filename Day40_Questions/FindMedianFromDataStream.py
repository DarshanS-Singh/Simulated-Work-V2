# Question Link:- https://leetcode.com/problems/find-median-from-data-stream/description/?envType=study-plan-v2&envId=top-interview-150

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0


# Solution Class
class MedianFinder(object):

    def __init__(self):
        self.minHeapForLargeNum = []
        self.maxHeapForSmallNum = []

        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxHeapForSmallNum) == 0 or -self.maxHeapForSmallNum[0] >= num:
            heapq.heappush(self.maxHeapForSmallNum, -num)
        else:
            heapq.heappush(self.minHeapForLargeNum, num)
        
        if len(self.maxHeapForSmallNum) > len(self.minHeapForLargeNum) + 1:
            heapq.heappush(
                self.minHeapForLargeNum, -heapq.heappop(self.maxHeapForSmallNum)
            )
        elif len(self.maxHeapForSmallNum) < len(self.minHeapForLargeNum):
            heapq.heappush(
                self.maxHeapForSmallNum, -heapq.heappop(self.minHeapForLargeNum)
            )

        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeapForSmallNum) == len(self.minHeapForLargeNum):
            return (-self.maxHeapForSmallNum[0] + self.minHeapForLargeNum[0]) / 2.0
        else:
            return -self.maxHeapForSmallNum[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()