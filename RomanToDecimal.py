def romanToDecimal(s):
    total = 0
    letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    while i < len(s) - 1:
        c, n = s[i], s[i + 1]
        if letters[c] < letters[n] and i + 1 == len(s) - 1:
            total += letters[n] - letters[c]
            i += 2
            break
        if letters[c] < letters[n]:
            total += letters[n] - letters[c]
            i += 2
        else:
            total += letters[c]
            i += 1
    if i == len(s) - 1:
        total += letters[s[-1]]
    return total