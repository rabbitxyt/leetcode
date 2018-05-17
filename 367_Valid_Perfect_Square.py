# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#


import math


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if math.sqrt(num).is_integer():
            return True
        else:
            return False