# Suppose Andy and Doris want to choose a restaurant for dinner,
# and they both have a list of favorite restaurants represented by strings.
#
# You need to help them find out their common interest with the least list index sum.
# If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        d = dict()

        for i in range(len(list1)):
            if list1[i] in list2:
                d[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in d:
                d[list2[j]] += j

        def minimums(some_dict):
            positions = []  # output variable
            min_value = float("inf")
            for k, v in some_dict.items():
                if v == min_value:
                    positions.append(k)
                if v < min_value:
                    min_value = v
                    positions = []  # output variable
                    positions.append(k)

            return positions

        m = minimums(d)

        return m