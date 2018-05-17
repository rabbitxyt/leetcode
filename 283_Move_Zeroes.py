# Given an array nums, write a function to move all 0's to the end
# of it while maintaining the relative order of the non-zero elements.
#


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        idx = 0
        while 0 in nums:
            nums.remove(0)
            idx += 1

        for i in range(idx):
            nums.append(0)