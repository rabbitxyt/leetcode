# Given a string S and a character C, return an array of integers representing the shortest distance
# from the character C in the string.
#
#


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        l = []

        for i in range(len(S)):
            if S[i] == C:
                l.append(i)

        ans = []

        for j in range(len(S)):
            temp = min(l, key=lambda x: abs(x - j))
            ans.append(abs(j - temp))

        return ans