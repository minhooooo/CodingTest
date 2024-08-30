import sys
from collections import deque

n,k=map(int,input().split())

cnt=[0]*100001
visited=[0]*100001

def bfs(node,end):
    queue=deque()
    queue.append(node)
    while queue:
        node=queue.popleft()
        if node==end:
            print(cnt[node]) 
            exit()
        if -1<node*2<100001 and visited[node*2]==0 :
            queue.appendleft(node*2)
            cnt[node*2]=cnt[node]
            visited[node*2]=1
        if -1<node-1<100001 and visited[node-1]==0 :
            queue.append(node-1)
            cnt[node-1]=cnt[node]+1
            visited[node-1]=1
        if -1<node+1<100001 and visited[node+1]==0 :
            queue.append(node+1)
            cnt[node+1]=cnt[node]+1
            visited[node+1]=1



bfs(n,k)