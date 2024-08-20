import heapq
import sys

input=sys.stdin.readline

hq=[]

for i in range(int(input())):
    temp=int(input())
    if temp!=0:
        heapq.heappush(hq,temp*(-1))
    else:
        if hq:
            print(heapq.heappop(hq)*(-1))
        else:
            print("0")