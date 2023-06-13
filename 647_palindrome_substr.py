class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0

        for i in range(len(s)):  # iterate center of palindrome
            left, right = i, i  # odd len palindrome
            while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                count += 1
                left -= 1
                right += 1
            
            left, right = i, i+1  # even len palindrome
            while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                count += 1
                left -= 1
                right += 1
        
        return count