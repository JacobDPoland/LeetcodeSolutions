class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_dict = {}
        
        # count the letters in s by incrementing counters
        for letter in s:
            if letter in count_dict.keys():
                count_dict[letter] += 1
            else:  # first time assignment
                count_dict[letter] = 1
        
        # decrement counter for letters in t
        for letter in t:
            if not (letter in count_dict.keys()):
                return False
            # if t has an extra letter
            elif count_dict[letter] == 0: 
                return False
            else:
                count_dict[letter] -= 1
        
        # if any count is not zero, then it is not an anagram
        for key in count_dict.keys():
            if not (count_dict[key] == 0):
                return False
        
        # if the process reaches this point, then the inputs are anagrams
        return True   
                
        
        
        