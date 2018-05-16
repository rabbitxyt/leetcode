# Write a function that takes an unsigned integer
# and returns the number of '1' bits it has
# (also known as the Hamming weight).


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        n = str(bin(n)[2:]).count('1')

        return n