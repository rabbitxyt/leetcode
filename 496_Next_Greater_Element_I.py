# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements
# are subset of nums2. Find all the next greater numbers for nums1's elements in the
# corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its
# right in nums2. If it does not exist, output -1 for this number.
#


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []

        for i in range(len(nums1)):
            idx_in_nums2 = nums2.index(nums1[i])
            ans.append(-1)
            for j in range(idx_in_nums2 + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans[-1] = nums2[j]
                    break

        return ans