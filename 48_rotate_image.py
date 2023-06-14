class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bot = left, right

                # save top left
                topLeft = matrix[top][left + i]
                # move bottom left into top left
                matrix[top][left + i] = matrix[bot - i][left]

                # save top right
                topRight = matrix[top + i][right]
                # move top left to top right
                matrix[top + i][right] = topLeft

                # save bottom right
                botRight = matrix[bot][right - i]
                # move top right to bottom right
                matrix[bot][right - i] = topRight

                # move bottom right into bottom left
                matrix[bot - i][left] = botRight

            left += 1
            right -= 1