import sys
import itertools

input=sys.stdin.readline

n = int(input())
arr=[]
cost=[]
for i in range(n):
    arr.append(list(map(int,input().strip().split())))
    cost.append([0,0,0])

cost[0]=arr[0]
for i in range(1,n):
    cost[i][0]=min(cost[i-1][2],cost[i-1][1])+arr[i][0]
    cost[i][1]=min(cost[i-1][0],cost[i-1][2])+arr[i][1]
    cost[i][2]=min(cost[i-1][0],cost[i-1][1])+arr[i][2]

print(min(cost[n-1]))