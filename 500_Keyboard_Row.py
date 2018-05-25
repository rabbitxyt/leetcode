# Given a List of words, return the words that can be typed using letters of alphabet
# on only one row's of American keyboard like the image below.
#



class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        ans = []

        for i in words:
            s = set()
            for j in i.lower():
                if j in set1:
                    s.add(1)
                elif j in set2:
                    s.add(2)
                elif j in set3:
                    s.add(3)
            if len(s) == 1:
                ans.append(i)

        return ans
