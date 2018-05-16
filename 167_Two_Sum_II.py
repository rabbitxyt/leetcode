# Given an array of integers that is already sorted
# in ascending order, find two numbers such that they
# add up to a specific target number.
#
# The function twoSum should return indices of the two
# numbers such that they add up to the target,
# where index1 must be less than index2.
#
#
# Note:
#
# Your returned answers (both index1 and index2) are not
#  zero-based.
# You may assume that each input would have exactly one
# solution and you may not use the same element twice.
#



class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        new_numbers = []
        d = dict()
        for k in range(len(numbers)):
            if numbers[k] not in d:
                d[numbers[k]] = 1
            else:
                d[numbers[k]] += 1
            if d[numbers[k]] <= 2:
                new_numbers.append(numbers[k])

        for i in range(len(new_numbers) - 1):
            for j in range(i + 1, len(new_numbers)):
                s = new_numbers[i] + new_numbers[j]
                if s > target:
                    break
                elif s == target:
                    if new_numbers[i] == new_numbers[j]:
                        return numbers.index(new_numbers[i]) + 1, numbers.index(new_numbers[j]) + 2
                    else:
                        return numbers.index(new_numbers[i]) + 1, numbers.index(new_numbers[j]) + 1
