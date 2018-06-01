# X is a good number if after rotating each digit individually
# by 180 degrees, we get a valid number that is different from X.
# Each digit must be rotated - we cannot choose to leave it alone.
#


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        def is_good_number(num):
            new_str = ''
            str_num = str(num)
            for x in str(num):
                if int(x) in (0, 1, 8):
                    new_str += x
                elif int(x) in (2, 5):
                    new_str += str(7 - int(x))
                elif int(x) in (6, 9):
                    new_str += str(15 - int(x))
                else:
                    return False
            if new_str != str_num:
                return True
            else:
                return False

        cnt = 0
        for i in range(1, N + 1):
            if is_good_number(i):
                cnt += 1
        return cnt