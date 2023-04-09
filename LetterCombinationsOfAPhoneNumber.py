# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
import itertools


def letterCombinations(digits):
    letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    nums = []
    for i in digits:
        nums.append(letters[i])
    combinations = [''.join(p) for p in itertools.product(*nums)]
    return combinations


s = input()
print(letterCombinations(s))
