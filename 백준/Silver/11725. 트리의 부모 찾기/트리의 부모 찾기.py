import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
node_dic=dict()
level=dict()

for i in range(n-1):
    a,b=map(int,input().strip().split())
    node_dic.setdefault(a,[])
    node_dic.setdefault(b,[])
    node_dic[a].append(b)
    node_dic[b].append(a)

check=[1]*(n+1)
parent=[-1]*(n+1)
que=deque()
def BFS(node):
    que.append(node)
    while que:
        temp=que.popleft()
        if check[temp]==0:
            continue
        check[temp]=0
        for i in node_dic[temp]:
            if check[i]:
                que.append(i)
                parent[i]=temp
        

BFS(1)
for i in range(2,n+1):
    print(parent[i])