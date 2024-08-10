import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write
a=int(input())
temp=deque()
for i in range(1,a+1,1):
    temp.append(i)
for _ in range(a-1):
    temp.popleft()
    temp.append(temp.popleft())
print(str(temp[0]))