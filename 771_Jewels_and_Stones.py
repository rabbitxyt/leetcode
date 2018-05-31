# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.  Each character in S is a type of
# stone you have.  You want to know how many of the stones you have are also
# jewels.
#


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        str_J = []
        for i in J:
            str_J.append(i)

        cnt = 0

        for j in S:
            if j in str_J:
                cnt += 1

        return cnt