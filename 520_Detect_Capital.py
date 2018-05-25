# Given a word, you need to judge whether the usage of capitals in it
# is right or not.
#


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        s = set()

        for i in range(len(word)):
            if i == 0 and word[i].isupper():
                s.add(0)
            elif word[i].isupper():
                s.add(1)
            elif word[i].islower():
                s.add(2)

        correct_list = [{0, 2}, {0, 1}, {0}, {2}]

        if s in correct_list:
            return True
        else:
            return False