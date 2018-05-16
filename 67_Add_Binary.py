# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        ab = int(a, 2)
        bb = int(b, 2)
        cb = ab + bb

        c = bin(cb)[2:]
        return c