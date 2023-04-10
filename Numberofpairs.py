#https://codeforces.com/problemset/problem/1538/C

t=int(input())
for k in range(t):
    n,l,r=map(int,input().split())
    li=list(map(int,input().split()))
    li.sort()
    i=0
    j=n-1
    a=0
    while(i<j):
        if(li[i]+li[j]<=r):
            a=a+(j-i)
            i=i+1
        else:
            j=j-1

    z=0
    y=n-1
    b=0
    while(z<y):
        if(li[z]+li[y]<=l-1):
            b=b+(y-z)
            z=z+1
        else:
            y=y-1
    
    print(a-b)