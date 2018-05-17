# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j
# in the array such that nums[i] = nums[j] and the absolute
# difference between i and j is at most k.



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)

        ans = False
        for m, n in d.items():
            if len(n) > 1:
                for p in range(1, len(n)):
                    s = n[p] - n[p - 1]
                    if s <= k:
                        ans = True
                        break

        return ans