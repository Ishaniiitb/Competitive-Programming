def search(haystack: str, needle):
    n_int = int(needle, 36)
    n = len(needle)
    for i in range(len(haystack)-n+1):
        h_int = int(haystack[i:i+n], 36)
        if h_int == n_int:
            return i
    return -1
