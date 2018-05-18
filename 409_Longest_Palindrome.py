# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = dict()

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        ans = 0
        f = 0

        for k in d:
            if d[k] % 2 == 1:
                f = 1
            ans += d[k] - d[k] % 2

        return ans + f