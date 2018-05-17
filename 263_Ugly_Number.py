# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        ans = True

        if num < 1:
            ans = False
        else:
            while num > 1:
                if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
                    if num % 2 == 0:
                        num = num // 2
                    if num % 3 == 0:
                        num = num // 3
                    if num % 5 == 0:
                        num = num // 5
                else:
                    ans = False
                    break

        return ans