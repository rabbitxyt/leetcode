# You have a total of n coins that you want to form in a staircase shape,
# where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#



class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 0
        j = 0
        if n == 0:
            return 0
        else:
            while i < n:
                j += 1
                i += j
                if i == n:
                    return j
                elif i > n:
                    return j - 1