# Given a string s consists of upper/lower-case alphabets
# and empty space characters ' ', return the length of last word
# in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of
# non-space characters only.



class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.split(' ')

        if not any(s):
            return 0
        if '' in s:
            s = [i for i in s if i != '']
        return len(s[-1])  