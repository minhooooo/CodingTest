import sys
import math

input=sys.stdin.readline

test=int(input())
for _ in range(test):
    clothes=dict()
    for _ in range(int(input())):
        name, kind=map(str,input().strip().split())
        clothes.setdefault(kind,0)
        clothes[kind]+=1
    temp=1
    for i in clothes.keys():
        temp=temp*(clothes[i]+1)
    print(int(temp-1))