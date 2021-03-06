# Assume you are an awesome parent and want to give your children some cookies. But, you should
# give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size
# of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi,
# we can assign the cookie j to the child i, and the child i will be content. Your goal is to
# maximize the number of your content children and output the maximum number.

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        ans = 0

        g.sort()
        s.sort()

        for i in range(len(g)):
            for j in s:
                if j >= g[i]:
                    ans += 1
                    s.remove(j)
                    break

        return ans