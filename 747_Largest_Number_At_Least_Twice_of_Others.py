# In a given integer array nums, there is always exactly one largest element.
#
# Find whether the largest element in the array is at least twice as much as
# every other number in the array.
#
# If it is, return the index of the largest element, otherwise return -1.
#



class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_num = max(nums)

        max_num_index = nums.index(max_num)

        nums.pop(max_num_index)

        flag = True

        for i in nums:
            if max_num >= 2 * i:
                pass
            else:
                flag = False
                break

        if flag:
            return max_num_index
        else:
            return -1
