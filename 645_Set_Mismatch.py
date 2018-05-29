# The set S originally contains numbers from 1 to n. But unfortunately,
# due to the data error, one of the numbers in the set got duplicated to
# another number in the set, which results in repetition of one number
# and loss of another number.
#
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
#


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        c = set()
        for i in range(len(nums)):
            c.add(i + 1)

        s = set(nums)

        for i in (c - s):
            m = i

        n = m - ((1 + len(nums)) * len(nums) / 2 - sum(nums))

        return [n, m]