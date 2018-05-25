# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.
#

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        bin_num = bin(num)[2:]

        bin_ones = ''

        for i in range(len(bin_num)):
            bin_ones += '1'

        bin_comp = str(int(bin_ones) - int(bin_num))

        return int(bin_comp, 2)