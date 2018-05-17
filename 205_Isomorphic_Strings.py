# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s
# can be replaced to get t.
#
# All occurrences of a character must be replaced with
# another character while preserving the order of
# characters. No two characters may map to the same
# character but a character may map to itself.



class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        def str_to_num(k):
            a = []
            for i in range(len(k)):
                if k[i] not in a:
                    a.append(k[i])
            b = ''
            for j in range(len(k)):
                b += str(a.index(k[j]))
            return b


        if str_to_num(s) == str_to_num(t):
            return True
        else:
            return False