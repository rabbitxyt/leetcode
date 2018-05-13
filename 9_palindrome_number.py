# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = True
        if x < 0:
            flag = False
        else:
            x = str(x)
            l = len(x)
            for i in range(l):
                if x[i] != x[l-1-i]:
                    flag = False
                    break
        return flag

# Follow up:
#
# Coud you solve it without converting the integer to a string?

