import sys

input=sys.stdin.readline

N,K=map(int,input().split())
coin=[]
count=0
for _ in range(N):
    coin.append(int(input().strip()))
for i in range(N-1,-1,-1):
    if K//coin[i]>=1:
        count+=K//coin[i]
        K=K-(K//coin[i])*coin[i]
        if K==0:
            print(count)
            exit()  
