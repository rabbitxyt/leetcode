# Given a non-empty array of digits representing a non-negative integer,
# plus one to the integer.
#
# The digits are stored such that the most significant digit
# is at the head of the list, and each element in the array contain
# a single digit.
#
# You may assume the integer does not contain any leading zero,
# except the number 0 itself.
#


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        str1 = ''
        for i in range(len(digits)):
            str1 += str(digits[i])
        int1 = int(str1)
        int2 = int1 + 1
        str2 = str(int2)
        ans = []
        for i in range(len(str2)):
            ans.append(int(str2[i]))
        return ans