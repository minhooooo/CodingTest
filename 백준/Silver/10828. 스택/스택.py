from collections import deque
import sys
input=sys.stdin.readline
print=sys.stdout.write

que=deque()
size=0
for _ in range(int(input())):
    a=list(input().split())
    if a[0] == 'push':
        que.append(a[1])
        size+=1
    elif a[0] == 'pop':
        if size==0:
            print("-1\n")
        else:
            size-=1
            print(str(que.pop())+"\n")
    elif a[0] == 'size':
        print(str(size)+"\n")
    elif a[0] == 'empty':
        if size:
            print("0\n")
        else:
            print("1\n")
    elif a[0] == 'top':
        if size==0:
            print("-1\n")
        else:
            print(str(que[-1])+"\n")