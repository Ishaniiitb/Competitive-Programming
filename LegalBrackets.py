def isValid(s):
    stack = []
    o_brackets = {"(": ")", "{": "}", "[": "]"}
    for i in s:
        if not stack:
            stack.append(i)
        elif i in o_brackets:
            stack.append(i)
        elif stack[-1] in o_brackets and i == o_brackets[stack[-1]]:
            stack.pop()
        else:
            break
    if stack:
        return False
    else:
        return True
