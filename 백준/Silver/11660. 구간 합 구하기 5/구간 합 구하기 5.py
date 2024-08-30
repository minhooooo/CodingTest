import sys
from collections import deque 
input=sys.stdin.readline

n,m=map(int,input().strip().split())
arr=[]
accumulate=[[0]*n for i in range(n)]
for _ in range(n):
    arr.append(list(map(int,input().strip().split())))

accumulate[0][0]=arr[0][0]
for j in range(1,n):
    accumulate[0][j]=arr[0][j]+accumulate[0][j-1]

for i in range(1,n):
    accumulate[i][0]=arr[i][0]+accumulate[i-1][0]
    for j in range(1,n):
        accumulate[i][j]=arr[i][j]+accumulate[i][j-1]+accumulate[i-1][j]-accumulate[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2=map(int,input().strip().split())
    temp=0
    if x1==1:
        if y1==1:
            temp=accumulate[x2-1][y2-1]
        else:
            temp=accumulate[x2-1][y2-1]-accumulate[x2-1][y1-2]
    else:
        if y1==1:
            temp=accumulate[x2-1][y2-1]-accumulate[x1-2][y2-1]
        else:
            temp=accumulate[x2-1][y2-1]-accumulate[x2-1][y1-2]-accumulate[x1-2][y2-1]+accumulate[x1-2][y1-2]
    print(temp)
