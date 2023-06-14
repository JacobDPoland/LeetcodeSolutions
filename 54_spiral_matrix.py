class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        seen = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top, bottom = 0, ROWS
        left, right = 0, COLS

        res = []

        while left < right and bottom > top:
            # top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # done with a row

            # right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # done with a col


            # check condition again after slicing off a corner
            # to ensure program doesn't go out of bounds
            if not(left < right and bottom > top):
                break
            

            # bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # done with a row

            # left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # done with left col
            
        return res
            