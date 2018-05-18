# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
#


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = s.split()

        return len(l)