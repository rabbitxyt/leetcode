# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 1
        end = n

        def cut_half(s, e):
            h = (s + e) // 2
            if isBadVersion(h):
                e = h
            else:
                s = h + 1
            return s, e

        while start != end:
            start, end = cut_half(start, end)

        return start