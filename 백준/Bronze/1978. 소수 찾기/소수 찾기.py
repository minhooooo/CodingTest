import sys
import math
input=sys.stdin.readline
print=sys.stdout.write
a=input()
temp=list(map(int,input().split()))
count=0
for i in temp:
    flag=0
    if i==1:
        continue
    if i==2:
        count+=1
        continue
    for k in range(2,math.ceil(math.sqrt(i))+1):
        if i%k==0:
            flag=1
            break
    if flag==0:
        count+=1
print(str(count))