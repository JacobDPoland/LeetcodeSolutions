class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        time complexity: O(m * n * 4^15) where 15 is the max length of the word
                         as defined in the problem description
        """
        
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            """
            r: current row number
            c: currenet column number
            i: current index of word
            """
            if i == len(word):
                return True
            
            # bounds checking
            if (r < 0) or (c < 0) or (r >= ROWS) or (c >= COLS):
                return False
            # picked the wrong letter
            elif word[i] != board[r][c]:
                return False
            # be sure not to reuse tiles
            elif (r, c) in path:
                return False
            
            path.add((r, c))  # add current tile to path
            # run dfs on all possible movements
            res = ( dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1)
            )

            # remove current tile after all possible movements from this
            # tile have been explored
            path.remove((r, c))

            return res  # returns true if only one of the dfs functions return true
        # end of dfs function

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        
        # else everthing has been explored
        return False
    # end of exist function 
            