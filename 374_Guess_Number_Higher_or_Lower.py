# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n

        def cut_half(s, e):
            h = (s + e) // 2
            if guess(h) == 1:
                return h + 1, e
            elif guess(h) == -1:
                return s, h - 1
            elif guess(h) == 0:
                return h, h

        while start != end:
            start, end = cut_half(start, end)

        return start