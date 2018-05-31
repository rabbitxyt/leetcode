# Given a positive integer, check whether it has alternating bits:
# namely, if two adjacent bits will always have different values.
#


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        b = bin(n)[2:]

        l = [int(i) for i in b]

        flag = True

        for i in range(len(l)):
                if i % 2 == 0:
                    if l[i] == 1:
                        pass
                    else:
                        flag = False
                        break
                if i % 2 == 1:
                    if l[i] == 0:
                        pass
                    else:
                        flag = False
                        break

        return flag