import sys

input=sys.stdin.readline

arr=list(input().strip())

stack=[]
ans=[]
flag=0

for i in arr:
    if i=='<':
        while stack:
            ans.append(stack.pop())
        flag=1
        ans.append(i)
    elif i=='>':
        flag=0
        ans.append(i)
    elif flag==1:
        ans.append(i)
    elif i==' ':
        while stack:
            ans.append(stack.pop())
        ans.append(" ")
    elif flag==0:
        stack.append(i)
while stack:
    ans.append(stack.pop())
print("".join(ans))