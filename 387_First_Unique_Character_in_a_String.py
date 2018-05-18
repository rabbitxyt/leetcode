# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.



class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = []
        a = set()
        b = set()
        ans = set()
        idx = None

        for i in range(len(s)):
            if s[i] not in a and s[i] not in b:
                a.add(s[i])
                ans.add(i)
            elif s[i] in a:
                a.discard(s[i])
                ans.discard(s.index(s[i]))
                b.add(s[i])

        if len(ans) != 0:
            return min(ans)
        else:
            return -1
