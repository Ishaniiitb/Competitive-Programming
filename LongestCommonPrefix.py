def commonPrefix(strs):
    common = []
    flag = True
    shortest, l = "", 10000
    for i in strs:
        if len(i) < l:
            shortest = i
            l = len(i)
    for i in range(l):
        for j in strs:
            if j[i] != shortest[i]:
                flag = False
                break
        if flag:
            common.append(shortest[i])
        else:
            break
    return "".join(common)