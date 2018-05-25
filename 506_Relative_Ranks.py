# Given scores of N athletes, find their relative ranks and the people
# with the top three highest scores, who will be awarded medals: "Gold Medal",
# "Silver Medal" and "Bronze Medal".
#


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        nums_sorted = sorted(nums, reverse=True)

        ans = []

        for i in nums:
            if nums_sorted.index(i) == 0:
                ans.append("Gold Medal")
            elif nums_sorted.index(i) == 1:
                ans.append("Silver Medal")
            elif nums_sorted.index(i) == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(nums_sorted.index(i) + 1))

        return ans