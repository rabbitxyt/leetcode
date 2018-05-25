# # You are given a string representing an attendance record for a student.
# # The record only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.

# A student could be rewarded if his attendance record doesn't contain
# more than one 'A' (absent) or more than two continuous 'L' (late).


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if "LLL" in s:
            return False
        if s.count("A") > 1:
            return False
        else:
            return True