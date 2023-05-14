class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        # O(t) efficency is 2^(t) where t = target
        def dfs(i, current, total):
            # base cases
            if total  == target:
                res.append(list(current))  # append a copy
                # res.append(current)
                return
            if i >= len(candidates) or total > target:
                return
            
            # recursive steps

            # case where candidates[i] is included in combo
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])

            # case wehre candidates[i] is NOT included in combo
            current.pop()
            dfs(i + 1, current, total)
            # returns implicitly
        
        # start dfs algorithm
        dfs(0, [], 0)
        return res