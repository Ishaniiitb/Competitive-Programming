#https://codeforces.com/problemset/problem/683/D

q = int(input())
ans = []

for i in range(q):
    n, m, p = map(int, input().split())

    arr = []

    for j in range(1, p):
        if (p % j) == 0:
            arr.append(j)

    flag = 0

    for item in arr:
        if flag == 0:
            if (item <= (n or m)) and ((p // item) <= (n or m)):
                flag = 1

    if flag == 1:
        ans.append("Yes")
    else:
        ans.append("No")

for item in ans:
    print(item)
