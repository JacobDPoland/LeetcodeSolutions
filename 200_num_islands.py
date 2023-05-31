from collections import deque
class Solution(object): 
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        seen = [ [False]*COLS for i in range(ROWS) ]  # bit/bool map tracking seen tiles
        island_count = 0

        def bfs(x, y):
            """
            x: initial row
            y: initial column
            """
            queue = deque([(x, y)])
            while len(queue) != 0:
                row, col = queue.popleft()  # get current row and column

                # bfs branch ends if it encounters a 0 or a previously seen tile
                if grid[row][col] == "0" or seen[row][col]:
                    continue
                # else == 1

                seen[row][col] = True
                
                # append tile to the north
                if row - 1 >= 0:
                    queue.append((row - 1, col))
                # append tile to the south
                if row + 1 < ROWS:
                    queue.append((row + 1, col))
                # append tile to the east
                if col + 1 < COLS:
                    queue.append((row, col + 1))
                # append tile to the west
                if col - 1 >= 0:
                    queue.append((row, col - 1))
        # end of bfs function                


        for i in range(ROWS): 
            for j in range(COLS):
                if grid[i][j] == "1" and not seen[i][j]:
                    bfs(i, j)  # explore whole island and track seen tiles
                    island_count += 1
        return island_count
    # end of numIslands function
# end of Solution class


if __name__ == "__main__":
    pass