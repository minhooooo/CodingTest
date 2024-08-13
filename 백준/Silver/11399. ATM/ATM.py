import sys
input=sys.stdin.readline
print=sys.stdout.write
a=int(input())
temp=sorted(list(map(int,input().split())))
result=0
for i in range(a):
    result=result+(a-i)*temp[i]
print(str(result))