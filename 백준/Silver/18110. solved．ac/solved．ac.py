import math
import sys

input=sys.stdin.readline
print=sys.stdout.write

count=int(input())
size=count
temp=dict()
for _ in range(count):
    ins=int(input())
    temp.setdefault(ins,0)
    temp[ins]+=1
key=sorted(temp.keys())
status=math.floor(count*0.15+0.5)
for i in range(status):
    if temp[key[0]]<=1:
        del key[0]
    else:
        temp[key[0]]-=1
    if temp[key[-1]]<=1:
        del key[-1]
    else:
        temp[key[-1]]-=1
    size-=2
sum=0
if count>0:
    for i in key:
        sum+=i*temp[i]
    print(str(math.floor(sum/size+0.5)))
else:
    print("0")