#https://codeforces.com/problemset/problem/1324/D

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append(a[i]-b[i])

c.sort()
i=0
j=n-1
count=0
while(i<j):
    if (c[i]+c[j]>0):
        count=count+(j-i)
        j=j-1
    else:
        i=i+1

print(count)    