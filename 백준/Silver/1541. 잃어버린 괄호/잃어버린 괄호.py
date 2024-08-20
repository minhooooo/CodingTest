import sys

input=sys.stdin.readline

ori=input().strip().split('-')

num=[]
flag=0
for i in ori:
    for k in i.strip().split('+'):
        flag+=int(k)
    num.append(flag)
    flag=0
result=num[0]
for i in range(1,len(num)):
    result-=num[i]
print(result)
