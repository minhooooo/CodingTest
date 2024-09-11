import sys

input=sys.stdin.readline

n,m,r,c,k = map(int,input().strip().split())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

lst = list(map(int,input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0,0,0,0,0,0]

def turn(i):
    if i == 1: 
       dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[5], dice[1], dice[4], dice[3], dice[0], dice[2]              
    elif i == 2: 
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]
    elif i == 3: 
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]
    else: 
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]

for i in lst:
    nr = r + dx[i-1]
    nc = c + dy[i-1]
    if 0 <= nr < n and 0 <= nc < m:
        turn(i)
        print(dice[2])
        if data[nr][nc] == 0:
            data[nr][nc] = dice[0]
        else:
            dice[0] = data[nr][nc]
            data[nr][nc] = 0
    else:
        nr -= dx[i-1]
        nc -= dy[i-1]
        continue
    r,c = nr,nc