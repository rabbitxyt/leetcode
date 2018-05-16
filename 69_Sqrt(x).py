# Implement int sqrt(int x).
#
# Compute and return the square root of x,
# where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer,
# the decimal digits are truncated and only the integer part
# of the result is returned.

import math

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))