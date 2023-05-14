import heapq
class MedianFinder(object):

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # multiply num by negative one for all input/output of left_heap
        # so that it acts like a max heap instead of a min heap
        
        heapq.heappush(self.left_heap, -1 * num)  # always push to left initially
        
        # move top element of left_heap if (right_heap is empty) or (top element of left_heap
        # is greater than top element of right_heap)
        if (len(self.right_heap) == 0) or (self.right_heap[0] < (-1 * self.left_heap)):
            heappush(self.right_heap, -1 * heapq.heappop(self.left_heap))

        # rebalance as needed
        if len(self.right_heap) - len(self.left_heap) > 1: 
            heappush(self.left_heap, -1 * heapq.heappop(self.right_heap))
        elif len(self.left_heap) - len(self.right_heap) > 1:
            heappush(self.right_heap, -1 * heapq.heappop(self.left_heap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left_heap) > len(self.right_heap):  # left bigger than right
            return -1 * self.left_heap[0]
        elif len(self.right_heap) > len(self.left_heap):  # right bigger than left
            return self.right_heap[0]
        else:  # left same size as right
            average = ((-1 * self.left_heap[0]) + self.right_heap[0]) / 2.0
            print("(", (-1 * self.left_heap[0]), "+", self.right_heap[0], ") / 2 = ", average)
            return average
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()