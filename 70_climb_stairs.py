class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 3:
            return n
        
        n1 = 2
        n2 = 3

        for i in range(4, n+1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        
        return n2
