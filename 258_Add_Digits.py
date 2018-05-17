# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        def add_digits(n):
            n = str(n)
            if len(n) == 1:
                return int(n)
            else:
                s = 0
                for i in range(len(n)):
                    s += int(n[i])
                return s

        while len(str(num)) > 1:
            num = add_digits(num)

        return num