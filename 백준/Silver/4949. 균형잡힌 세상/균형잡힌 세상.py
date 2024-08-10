from collections import deque

temp=deque()
while 1:
    words=list(input())
    if words[0]=='.':
        break
    status=1
    temp.clear()
    for i in words:
        if i=='(' or i=='[':
            temp.append(i)
        elif i==')' or i==']':
            if len(temp)==0:
                status=0
                break
            pops=temp.pop()
            if i==')' and pops=='(':
                continue
            elif i==']' and pops=='[':
                continue
            else: 
                status=0
                break
    if status and len(temp)==0:
        print("yes")
    else:
        print("no")
                    