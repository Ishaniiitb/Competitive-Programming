# https://leetcode.com/problems/reverse-integer/
def reverse(self, x: int) -> int:
    smallest, biggest = -2 ** 31, 2 ** 31 - 1
    if x == 0:
        return 0
    num = str(x)
    flag = False
    if num[0] == '-':
        num = num[1:]
        flag = True
    l = len(num)
    index = 0
    for i in range(-1, -l - 1, -1):
        if num[i] == '0':
            index += 1
        else:
            break
    num = num[:l - index]
    num = int(num[::-1])
    if flag:
        num *= -1
    if smallest <= num <= biggest:
        return num
    else:
        return 0
