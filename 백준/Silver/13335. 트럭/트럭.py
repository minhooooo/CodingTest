import sys
from collections import deque

input=sys.stdin.readline
que=deque()
n,w,l=map(int,input().strip().split())
trucks=list(map(int,input().strip().split()))
for _ in range(w):
    que.append(0)
time=0
sum=0
i=0
while i<n:
    time+=1
    temp=que.popleft()
    if temp!=0:
        sum-=temp
    if sum+trucks[i]>l:
        que.append(0)
    else:
        que.append(trucks[i])
        sum+=trucks[i]
        i+=1
print(time+w)