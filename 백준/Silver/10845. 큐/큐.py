from collections import deque
import sys
input=sys.stdin.readline
print=sys.stdout.write

que=deque()
size=0
for _ in range(int(input())):
    inp=list(input().split())
    if inp[0]=='push':
        que.append(inp[1])
        size+=1
    elif inp[0]=='pop':
        if size==0:
            print("-1\n")
        else:
            size-=1
            print(str(que.popleft())+"\n")
    elif inp[0]=='size':
        print(str(size)+"\n")
    elif inp[0]=='empty':
        if size==0:
            print("1\n")
        else:
            print("0\n")
    elif inp[0]=='front':
        if size==0:
            print("-1\n")
        else:
            print(str(que[0])+"\n")
    elif inp[0]=="back":
        if size==0:
            print("-1\n")
        else:
            print(str(que[-1])+"\n")
    