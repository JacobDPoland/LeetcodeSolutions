class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = {x for x in nums}  # convert list to set  
        return not (len(nums) == len(nums_set))
        