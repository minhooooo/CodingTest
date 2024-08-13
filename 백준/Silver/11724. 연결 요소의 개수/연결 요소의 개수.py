import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
print=sys.stdout.write
a,b=map(int,input().split())
temp=[[] for _ in range(a+1)]
temp_search=[0]*(a+1)
def search(x):
    temp_search[x]=1
    for node in temp[x]:
        if temp_search[node]==0:
            search(node)
count=0
for _ in range(b):
    u,v=map(int,input().split())
    temp[u].append(v)
    temp[v].append(u)
for i in range(1,a+1):
    if temp_search[i]==0:
        count+=1
        search(i)
print(str(count))
    