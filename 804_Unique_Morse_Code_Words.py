# International Morse Code defines a standard encoding where each
# letter is mapped to a series of dots and dashes, as follows: "a"
# maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
#

# Return the number of different transformations among all words we have.


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        set_morse = set()

        for i in words:
            str_morse = ''
            for j in i:
                str_morse += m[ord(j) - 97]
            if str_morse not in set_morse:
                set_morse.add(str_morse)

        return len(set_morse)