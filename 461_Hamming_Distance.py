# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#



class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        x = bin(x)[2:].zfill(31)
        y = bin(y)[2:].zfill(31)

        ans = 0
        for i in range(0, 31):
            if x[i] != y[i]:
                ans += 1

        return ans