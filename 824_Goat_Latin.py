# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
#
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
#


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        S = S.split()

        ans = []

        for i in range(len(S)):
            if S[i].startswith(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
                temp = S[i] + 'ma'
            else:
                temp = S[i][1:] + S[i][0] + 'ma'

            for j in range(i + 1):
                temp += 'a'
            ans.append(temp)

        ans_str = ''

        for i in range(len(S)):
            ans_str += (ans[i] + ' ')

        return ans_str[:-1]