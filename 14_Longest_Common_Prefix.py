# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        op = ''

        if strs == []:
            return op
        else:
            l = len(strs[0])
            for i in range(len(strs)):
                if len(strs[i])<l:
                    l = len(strs[i])

            for j in range(l):
                f = None
                idx = 0
                for i in range(len(strs)):
                    if f is None:
                        f = strs[i][:1]
                        idx += 1
                    elif strs[i][:1] == f:
                        idx += 1
                    strs[i] = strs[i][1:]

                if idx == len(strs):
                    op += f
                else:
                    break


            return op