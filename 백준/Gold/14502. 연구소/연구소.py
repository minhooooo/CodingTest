import sys
import copy
from collections import deque
input= sys.stdin.readline

n,m=map(int,input().strip().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().strip().split())))

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def BFS():
    dq=deque()
    temp=copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if temp[i][j]==2:
                dq.append((i,j))
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and temp[nx][ny]==0:
                temp[nx][ny]=2
                dq.append((nx,ny))
    cnt=0
    for i in range(n):
        cnt+=temp[i].count(0)
    global ans
    ans=max(ans,cnt)

def wall(cnt):
    if cnt==3:
        BFS()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                arr[i][j]=1
                wall(cnt+1)
                arr[i][j]=0
ans=0
wall(0)
print(ans)