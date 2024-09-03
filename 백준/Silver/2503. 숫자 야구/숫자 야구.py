import sys
import itertools

input=sys.stdin.readline

n=int(input().strip())

case=list(itertools.permutations([str(i) for i in range(1,10)],3))

for _ in range(n):
    a,b,c=input().strip().split()
    a=list(str(a))
    revision=0
    for i in range(len(case)):
        strike=0
        ball=0
        i-=revision
        for j in range(3):
            if case[i][j]==a[j]:
                strike+=1
            elif a[j] in case[i]:
                ball+=1
        if strike!=int(b) or ball!=int(c):
            case.remove(case[i])
            revision+=1
print(len(case))