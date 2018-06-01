# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for i in range(len(A)):
            A[i].reverse()

        for j in range(len(A)):
            for k in range(len(A[j])):
                A[j][k] = 1 - A[j][k]

        return A