# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xs = str(abs(x))
        ys = str()
        for i in range(len(xs), 0, -1):
            ys += xs[i-1]
        y = int(ys)
        if y >= 2**31:
            return 0
        else:
            if x < 0:
                return -y
            else:
                return y