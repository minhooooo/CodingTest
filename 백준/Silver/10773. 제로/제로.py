from collections import deque

que=deque()
for _ in range(int(input())):
    temp=int(input())
    if temp!=0:
        que.append(temp)
    else:
        que.pop()
print(sum(que))