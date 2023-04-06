# https://leetcode.com/problems/string-to-integer-atoi/
def myAtoI(s):
    s = s.strip()
    if s == "":
        return 0
    smallest, largest = -2 ** 31, 2 ** 31 - 1
    num = ""
    negative, sign = False, False
    for i in s:
        if i == '-' and sign is False:
            negative = True
        elif i == '+' and sign is False:
            pass
        if i.isnumeric() is False:
            break
        else:
            num += i
        sign = True
    if num == "":
        return 0
    else:
        num = -1 * int(num) if negative else int(num)
    if num < smallest:
        return smallest
    elif num > largest:
        return largest
    return num
