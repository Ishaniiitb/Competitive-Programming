def isPalindrome(x):
    if x < 0:
        return False
    num, reverse = x, 0
    while num > 0:
        d = num % 10
        reverse = reverse * 10 + d
        num //= 10
    if reverse == x:
        return True
    else:
        return False
