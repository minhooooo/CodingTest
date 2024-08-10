import sys
from collections import deque
input = sys.stdin.readline
s,e = map(int,input().split())
if s==1:
    print(2)
    if e>=3:
        print(3)
elif s==2:
    print(2)
    if e>=3:
        print(3)
elif s==3: 
    print(3)
temp=[2,3]
if s>4:
    for i in range(4,s):
        root=int(i**(1/2))
        for k in temp:
            if i%k==0:
                break
            if k>root and i%k!=0:
                temp.append(i)
                break

for i in range(s,e+1):
    if i<=3:
        continue
    root=i**(1/2)
    
    for k in temp:
        if i%k==0:
            break
        if k>root and i%k!=0:
            temp.append(i)
            print(i)
            break