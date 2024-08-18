import sys
from collections import deque

input=sys.stdin.readline

def DFS(p):
    if check[p]:
        return
    check[p]=1
    DFS_result.append(p)
    for i in node.get(p,[]):
        DFS(i)

def BFS(q):
    while q:
        temp=q.popleft()
        if check[temp]:
            continue
        check[temp]=1
        BFS_result.append(temp)
        for i in node.get(temp,[]):
            q.append(i)

node=dict()

N,M,V=map(int,input().split())

for _ in range(M):
    a,b=map(int,input().split())
    node.setdefault(a,[])
    node.setdefault(b,[])
    node[a].append(b)
    node[b].append(a)
for i in node:
    node[i].sort()

check=[0]*(N+1)
DFS_result=[]
DFS(V)

check=[0]*(N+1)
BFS_result=[]
que=deque()
que.append(V)
BFS(que)

for i in DFS_result:
    print(i,end=" ")
print()
for i in BFS_result:
    print(i,end=" ")