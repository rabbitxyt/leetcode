# Suppose you have a long flowerbed in which some of the plots are planted
# and some are not. However, flowers cannot be planted in adjacent plots -
# they would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.
#


from math import ceil


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i in range(len(flowerbed)):
            if len(flowerbed) != 1:
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i + 1] == 1:
                        flowerbed[i] = -1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i] == 0 and flowerbed[i - 1] == 1:
                        flowerbed[i] = -1
                elif flowerbed[i - 1] == 1 or flowerbed[i + 1] == 1:
                    flowerbed[i] = -1

        k = 0
        m = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and i != len(flowerbed) - 1:
                k += 1
            elif flowerbed[i] != 0:
                m += ceil(float(k) / 2)
                k = 0
            elif flowerbed[i] == 0 and i == len(flowerbed) - 1:
                k += 1
                m += ceil(float(k) / 2)

        if m >= n:
            return True
        else:
            return False
