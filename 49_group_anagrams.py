class Solution(object):
    
    def checkAnagram(self, word1, word2):
        return ''.join(sorted(word1)) == ''.join(sorted(word2))
    
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()