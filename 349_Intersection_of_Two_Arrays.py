# Given two arrays, write a function to compute their intersection.


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []
        set1 = set(nums1)
        set2 = set(nums2)
        for i in set1:
            if i in set2:
                ans.append(i)
        return ans