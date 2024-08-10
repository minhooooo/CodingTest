import sys
from itertools import combinations
input=sys.stdin.readline
print=sys.stdout.write
temp={}
a=input()
a=list(input().split())
for i in a:
    temp.setdefault(i,0)
    temp[i]+=1
b=input()
b=list(input().split())
for i in b:
    temp.setdefault(i,0)
    print(str(temp[i])+" ")