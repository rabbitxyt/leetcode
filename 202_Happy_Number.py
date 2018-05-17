# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number
# by the sum of the squares of its digits, and repeat the
# process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include
# 1. Those numbers for which this process ends in 1 are
# happy numbers.



class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_sum(nums):
            nums = str(nums)
            s = 0
            for i in range(len(nums)):
                s += int(nums[i]) ** 2
            return s

        k = set()

        flag = True

        while n != 1:
            n = get_sum(n)
            if n not in k:
                k.add(n)
            else:
                flag = False
                break

        return flag