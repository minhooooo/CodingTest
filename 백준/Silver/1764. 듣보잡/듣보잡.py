import sys
input=sys.stdin.readline
print=sys.stdout.write
temp1=set()
temp2=set()
a,b=map(int,input().split())
for _ in range(a):
    temp1.add(input())
for _ in range(b):
    temp2.add(input())
result=sorted(temp1.intersection(temp2))
print(str(len(result))+"\n")
for i in result:
    print(str(i))