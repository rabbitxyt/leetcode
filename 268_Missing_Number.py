# Given an array containing n distinct numbers taken from
# 0, 1, 2, ..., n, find the one that is missing from the array.



class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        ans = int(l * (l + 1) / 2 - sum(nums))
        return ans
