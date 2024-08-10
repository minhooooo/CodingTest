import sys
from collections import deque
input = sys.stdin.readline
stack=deque()
flag=1
count=0
result=[]
for i in range(int(input())):
    target=int(input())
    if target>flag-1:
        for i in range(flag,target+1):
            stack.append(i)
            flag=flag+1
            i=i+1
            result.append("+")
            count=count+1
        stack.pop()
        result.append("-")
        count=count-1
    else :
        if count>0:
            if stack[-1]==target:
                stack.pop()
                count=count-1
                result.append("-")
            else :
                result.clear()
                result.append("NO")
                break
        else :
            result.clear()
            result.append("NO")
            break
for i in result:
    print(i)