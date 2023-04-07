# https://leetcode.com/problems/zigzag-conversion/
def convert(s, numRows):
    if numRows == 1:
        return s
    elif numRows == 2:
        return s[:len(s):2] + s[1:len(s):2]
    row, reverse = 0, False
    words = []
    for i in range(numRows):
        words.append([])
    i = 0
    while i < len(s):
        if row == numRows:
            reverse = True
            row -= 2
            continue
        words[row].append(s[i])
        if row < numRows and not reverse:
            row += 1
        else:
            row -= 1
        if row == 0:
            reverse = False
        i += 1
    word = ''
    for i in words:
        word += ''.join(i)
    return word


S = input()
n = int(input())
print(convert(S, n))
