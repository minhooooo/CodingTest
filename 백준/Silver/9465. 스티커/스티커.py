import sys
from collections import deque 
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    cost=[[0]*n for i in range(2)]
    arr=[]
    arr.append(list(map(int,input().strip().split())))
    arr.append(list(map(int,input().strip().split())))
    cost[0][0]=arr[0][0]
    cost[1][0]=arr[1][0]
    if n>=2:
        cost[0][1]=arr[0][1]+cost[1][0]
        cost[1][1]=arr[1][1]+cost[0][0]
        for i in range(2,n):
            cost[0][i]=arr[0][i]+max(cost[1][i-1],cost[0][i-2],cost[1][i-2])
            cost[1][i]=arr[1][i]+max(cost[0][i-1],cost[0][i-2],cost[1][i-2])
        print(max(cost[0][-1],cost[0][-2],cost[1][-1],cost[1][-2]))
    else:
        print(max(cost[0][-1],cost[1][-1]))