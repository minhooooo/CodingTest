import sys

input=sys.stdin.readline

n,k=map(int,input().strip().split())

arr=[i for i in range(n+1)]

count=0
for i in range(2,n+1):
    flag=1
    if arr[i]:
        while i*flag<=n:
            if arr[i*flag]:
                arr[i*flag]=0
                count+=1
            if count==k:
                print(i*flag)
                exit()
            flag+=1