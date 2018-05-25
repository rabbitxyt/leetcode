# Given a binary array, find the maximum number of consecutive 1s in this array.
#


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        c = []

        for i in range(len(nums)):
            if i == 0:
                if nums[i] == 1:
                    c.append(1)
                else:
                    c.append(0)
            else:
                if nums[i] == 1:
                    c.append(c[-1] + 1)
                else:
                    c.append(0)

        return max(c)