import sys
input=sys.stdin.readline
print=sys.stdout.write
a,b=map(int,input().split())
num=list(map(int,input().split()))
for i in range(1,a):
    num[i]=num[i-1]+num[i]
for _ in range(b):
    start,end=map(int,input().split()) 
    if start>=2:
        print(str(num[end-1]-num[start-2])+"\n")
    elif start>=1:
        print(str(num[end-1])+"\n")
