# Given an integer, write a function to determine if it is a power of three.

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0 or n == 2:
            return False
        elif n == 1:
            return True
        else:
            while n // 3 >= 1:
                if n % 3 == 0:
                    n = n // 3
                    if n == 1:
                        return True
                    if n == 2:
                        return False
                else:
                    return False