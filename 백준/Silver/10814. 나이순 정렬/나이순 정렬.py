import sys
from itertools import combinations
input=sys.stdin.readline
print=sys.stdout.write
temp={}
for _ in range(int(input())):
    a,b=input().split()
    temp.setdefault(int(a),[])
    temp[int(a)].append(b)
temp_keys=list(temp.keys())
temp_keys.sort()
for i in temp_keys:
    temp_values=temp[i]
    for k in temp_values:
        print(str(i)+" "+str(k)+"\n")