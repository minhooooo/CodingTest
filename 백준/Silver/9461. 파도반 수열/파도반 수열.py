import sys
import math

input=sys.stdin.readline

test=int(input())
for _ in range(test):
    N=int(input())
    tri=[1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if N>=10:
        for i in range(10,N):
            tri.append(tri[i-5]+tri[i-1])
    print(tri[N-1])