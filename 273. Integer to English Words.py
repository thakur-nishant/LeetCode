"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        lookup = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion'
        }
        result = ""
        p1 = 0
        while num:
            curr = num % 1000
            num = num // 1000
            curr_word = ""
            p2 = 0
            while curr:
                if curr == 0:
                    break
                if curr % 100 in lookup and p2 == 0:
                    curr_word += lookup[curr % 100]
                    curr //= 100
                    p2 = 2
                else:
                    if p2 == 0:
                        if curr % 10 != 0:
                            curr_word += lookup[curr % 10]
                        p2 += 1
                        curr //= 10
                    elif p2 == 1:
                        if curr % 10 != 0:
                            curr_word = lookup[curr % 10 * 10] + " " + curr_word
                        p2 += 1
                        curr //= 10
                    elif p2 == 2:
                        if curr_word:
                            curr_word = lookup[curr] + " Hundred " + curr_word
                        else:
                            curr_word = lookup[curr] + " Hundred"
                        curr //= 10
            if p1 != 0 and curr_word != "":
                result = curr_word + " " + lookup[10 ** p1] + " " + result
            elif curr_word != "":
                result = curr_word
            p1 += 3

        return result.strip()

