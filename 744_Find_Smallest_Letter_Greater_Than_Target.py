# Given a list of sorted characters letters containing only lowercase letters,
# and given a target letter target, find the smallest element in the list that
# is larger than the given target.
#
# Letters also wrap around. For example, if the target is target = 'z' and
# letters = ['a', 'b'], the answer is 'a'.
#



class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        letters_to_nums = []

        for i in letters:
            letters_to_nums.append(ord(i))

        target_to_nums = ord(target)

        flag = False
        for j in letters_to_nums:
            if j > target_to_nums:
                flag = True
                return chr(j)
                break

        if not flag:
            return chr(min(letters_to_nums))