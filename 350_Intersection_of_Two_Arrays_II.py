#
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []
        for i in nums1:
            if i in nums2:
                nums1[nums1.index(i)] = None
                nums2[nums2.index(i)] = None
                ans.append(i)

        return ans