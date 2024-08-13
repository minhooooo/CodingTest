import sys
input=sys.stdin.readline
print=sys.stdout.write
from collections import deque
test=int(input())
casex=[-1,0,1,0]
casey=[0,-1,0,1]
que=deque()

def search(temp,a,b):
    que.append([a,b])
    temp[a][b]=0
    while que: 
        a, b = que.popleft()
        for i in range(4):
            temp_x = a + casex[i]
            temp_y = b + casey[i]
            if 0<=temp_x<x and 0<=temp_y<y and temp[temp_x][temp_y] == 1: # 배추밭 범위를 벗어나지 않고 미방문한 좌표인 경우
                que.append([temp_x, temp_y])
                temp[temp_x][temp_y] = 0
                
for _ in range(test):
    x,y,total = map(int,input().split())
    temp=[[0]*y for _ in range(x)]
    for _ in range(total):
        a,b=map(int,input().split())
        temp[a][b]=1

    n=0
    for i in range(x):
        for j in range(y):
            if temp[i][j]==1:
                search(temp,i,j)
                n+=1
    print(str(n)+"\n")