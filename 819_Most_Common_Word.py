# Given a paragraph and a list of banned words, return the most frequent word that is not in the list
# of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer
# is unique.
#


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        chars = "!?',;."

        for c in chars:
            paragraph = paragraph.replace(c, '')
        paragraph_processed = paragraph.lower()

        print(paragraph_processed)

        d = dict()

        for i in paragraph_processed.split():
            if i in banned:
                pass
            elif i not in d:
                d[i] = 1
            else:
                d[i] += 1

        return max(d, key=d.get)