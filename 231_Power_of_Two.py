# Given an integer, write a function to determine if it is a power of two.


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        ans = False

        if n == 0:
            ans = False
        elif n == 1 or n == 2:
            ans = True
        else:
            while True:
                if n % 2 != 0:
                    break
                n = n // 2
                if n == 2:
                    ans = True
                    break

        return ans