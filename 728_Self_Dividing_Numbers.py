# A self-dividing number is a number that is divisible by every digit it contains.
#
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
#



class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        ans = []

        for i in range(left, right + 1):
            flag = True
            for j in str(i):
                if int(j) == 0:
                    flag = False
                    break
                else:
                    if i % int(j) != 0:
                        flag = False
                        break
            if flag:
                ans.append(i)

        return ans