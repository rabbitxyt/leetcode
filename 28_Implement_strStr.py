# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

haystack = "aaaaa"
needle = "bba"


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == '':
            return 0
        else:
            if needle in haystack:
                return haystack.find(needle)
            else:
                return -1