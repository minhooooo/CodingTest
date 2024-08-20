from collections import deque
import sys

input=sys.stdin.readline

N,M=map(int,input().strip().split())

school=[]
search=[[0]*M for _ in range(N)]

deq=deque()
go=[[-1,0],[1,0],[0,1],[0,-1]]

def BFS():
    count=0
    while deq:
        x,y=deq.popleft()
        if search[x][y]==1:
            continue
        search[x][y]=1
        if school[x][y]=="P":
            count+=1
        for dx,dy in go:
            if 0<=x+dx<N and 0<=y+dy<M:
                if search[x+dx][y+dy]==0 and school[x+dx][y+dy]!="X":
                    deq.append((x+dx,y+dy))
    if count:
        print(count)
    else:
        print("TT")
    exit()


for i in range(N):
    school.append(list(input().strip()))
for i in range(N):
    for j in range(M):
        if school[i][j]=="I":
            deq.append((i,j))
            BFS()


    
