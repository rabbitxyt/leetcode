# Given an array of size n, find the majority element.
# The majority element is the element that appears more
# than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the
# majority element always exist in the array.
#


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        d = dict()

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        for (key, val) in d.items():
            if val > len(nums) / 2:
                return key