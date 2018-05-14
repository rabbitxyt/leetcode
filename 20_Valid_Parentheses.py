# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        while any(q in s for q in ('()','[]','{}')):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')

        if s == '':
            return True
        else:
            return False