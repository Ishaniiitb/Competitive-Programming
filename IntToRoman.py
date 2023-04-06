# https://leetcode.com/problems/integer-to-roman/
def intToRoman(num):
    vals = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    tri, double, single = (1000, 500), (100, 50), (10, 5)
    roman = ''
    for i in vals:
        sub = ''
        d = num // i
        num -= d * i
        sub += vals[i] * d
        if i in tri and i > num > i-101:
            sub += 'C' + vals[i]
            num -= (i - 100)
        elif i in double and i > num > i-11:
            sub += 'X' + vals[i]
            num -= (i - 10)
        elif i in single and num == i-1:
            sub += 'I' + vals[i]
            num -= (i - 1)
        roman += sub
    return roman
