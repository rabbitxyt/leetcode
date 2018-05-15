# Given a sorted array and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#

nums = [1,3,5,6]
target = 0


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        min_val = min(nums)
        max_val = max(nums)

        if target <= min_val:
            return 0
        else:
            k = max([i for i in nums if i < target])
            return nums.index(k) + 1