import sys
from collections import deque 
input=sys.stdin.readline
print=sys.stdout.write

for _ in range (int(input())):
    n, m= map(int,input().split())
    temp=deque(map(int,input().split()))
    flag=temp[m]
    count=0
    upper=deque()
    for i in temp:
        if i>flag:
            count=count+1
            upper.append(i)
    step=0
    upper=deque(sorted(upper))
    while count>0:
        if temp[0]==upper[-1]:
            count=count-1
            upper.pop()
            step=step+1
            temp.popleft()
        else :
            temp.rotate(-1)
        m=m-1
        if m<0:
            m=n-step-1
    while m>=0:
        if flag==temp[0]:
            step=step+1
            temp.popleft()
        else :
            temp.rotate(-1)
        m=m-1

    print(str(step)+"\n")
