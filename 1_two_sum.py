class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_dict = {}
        for index1, val1 in enumerate(nums):
            diff = target - val1
            index2 = seen_dict.get(diff)
            if index2 != None:
                return [index1, index2]
            else:
                seen_dict[val1] = index1
            