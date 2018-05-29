# Initially, there is a Robot at position (0, 0).
# Given a sequence of its moves, judge if this robot makes a circle,
# which means it moves back to the original place.


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        p = [0,0]

        for i in range(len(moves)):
            if moves[i] == "U":
                p[1] += 1
            if moves[i] == "D":
                p[1] -= 1
            if moves[i] == "L":
                p[0] -= 1
            if moves[i] == "R":
                p[0] += 1

        if p == [0,0]:
            return True
        else:
            return False