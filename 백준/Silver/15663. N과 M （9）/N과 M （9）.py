import sys
import itertools

input=sys.stdin.readline

n,m = map(int,input().strip().split())
arr=list(map(int,input().strip().split()))

temp=sorted(set(itertools.permutations(arr,m)))

for i in temp:
    for j in i:
        print(j,end=' ')
    print()