import sys
input=sys.stdin.readline

a=int(input())

arr=[]
cost=[[0]*(i+1) for i in range(a)]
for i in range(a):
    arr.append(list(map(int,input().strip().split())))
cost[0]=arr[0]

for i in range(1,a):
    cost[i][0]=cost[i-1][0]+arr[i][0]
    for j in range(1,i):
        cost[i][j]=max(cost[i-1][j],cost[i-1][j-1])+arr[i][j]
    cost[i][-1]=cost[i-1][-1]+arr[i][-1]

print(max(cost[-1]))