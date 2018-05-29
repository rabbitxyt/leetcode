class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """

        l = []
        s = 0

        for i in range(len(ops)):
            if ops[i] == "C":
                n = l.pop()
                s -= n
            elif ops[i] == "D":
                s += l[-1] * 2
                l.append(l[-1] * 2)
            elif ops[i] == "+":
                s += l[-1] + l[-2]
                l.append(l[-1] + l[-2])
            else:
                a = int(ops[i])
                l.append(a)
                s += a

        return s